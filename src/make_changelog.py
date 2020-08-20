"""
Make a changelog from the repository's annotated git tags.

:usage: `python3 make_changelog.py --help`.
"""

import argparse, subprocess
from typing import Optional
import checks

def make_changelog(prefix: Optional[str] = None, file_name: str = "CHANGELOG.md") -> None:
	"""
	Make a changelog from the repository's git tags.

	:param prefix: Only use tags with this prefix.
	:param file_name: Name the created changelog file this.
	:raise subprocess.CalledProcessError: Failed to get tags.
	:raise AssertionError: The current working directory is not the root of a git repository.
	"""
	checks.assert_is_root()
	checks.assert_branch_exists()

	if prefix is None:
		prefix = ""

	versions = subprocess.run(["git", "tag", "--sort=-version:refname", "--list", f"{prefix}*", "--merged"], capture_output = True, check = True, text = True).stdout.split("\n")

	with open(file_name, "w") as f:
		f.write("# Changelog")

		for version in versions:
			version = version.strip()

			if version:
				date = subprocess.run(["git", "tag", "--list", "--format=%(taggerdate:format:%B %d, %Y)", version], capture_output = True, check = True, text = True).stdout.strip()
				f.write(f"\n\n## {version.lstrip(prefix)} ({date})")
				message = subprocess.run(["git", "tag", "--list", "--format=%(contents)", version], capture_output = True, check = True, text = True).stdout.strip()

				if message:
					f.write(f"\n\n{message}")

if __name__ == "__main__":
	_PARSER = argparse.ArgumentParser()
	_PARSER.add_argument("--prefix", default = None, help = "only use tags with this prefix")
	_PARSER.add_argument("--file-name", default = "CHANGELOG.md", help = "name the created file this")
	_ARGS = _PARSER.parse_args()
	make_changelog(prefix = _ARGS.prefix, file_name = _ARGS.file_name)