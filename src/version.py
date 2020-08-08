"""
Get the version of the current commit.

:usage: `python3 version.py --help`.
"""

import argparse, re, subprocess, sys
from typing import Optional
import checks

def get_version(prefix: Optional[str] = None, semver: bool = False, default: str = "0.0.0") -> str:
	"""
	Return the version of the current commit using git tags.

	:param prefix: Only consider tags with this prefix, and remove the prefix to get the version number.
	:param semver: Ensure the returned string is a Semantic Versioning 2.0 compliant string.
	:param default: Use this version if there is no version.
	:return: The version of the current commit. Include the full commit hash as metadata if it is not a release. Include a dirty indicator as metadata if there are uncommitted changes. For example, `1.0.0-beta.1+commit-5e94edf0845f6693683ab4e90b572d3a2967af1e.dirty`.
	:raise Exception: The version is not a Semantic Versioning 2.0 version (if `semver` is `True`).
	:raise subprocess.CalledProcessError: Failed to get tags, or a different shell command failed.
	:raise AssertionError: The current working directory is not the root of a git repository.
	"""
	checks.assert_is_root()

	try:
		checks.assert_branch_exists()
		branch_exists = True
	except AssertionError as e:
		print(f"Warning: {e}", file=sys.stderr)
		branch_exists = False

	if prefix is None:
		prefix = ""

	if branch_exists:
		version = subprocess.run(["git", "tag", "--sort=-version:refname", "--list", f"{prefix}*", "--merged"], capture_output = True, check = True, text = True).stdout.split("\n")[0].strip()
	else:
		version = None

	if version:
		current_commit_version = subprocess.run(["git", "tag", "--sort=-version:refname", "--points-at", "HEAD", "--merged"], capture_output = True, check = True, text = True).stdout.split("\n")[0].strip()
		is_release_commit = version == current_commit_version
	else:
		version = f"{prefix}{default}"
		is_release_commit = False

	version = version.lstrip(prefix)

	git_status = subprocess.run(["git", "status", "--porcelain"], capture_output = True, check = True, text = True).stdout.strip()
	is_dirty = bool(git_status)

	if is_dirty or not is_release_commit:
		metadata = []

		if branch_exists and not is_release_commit:
			current_commit_hash = subprocess.run(["git", "rev-parse", "--verify", "HEAD"], capture_output = True, check = True, text = True).stdout.strip()
			metadata.append(f"commit-{current_commit_hash}")

		if is_dirty:
			metadata.append("dirty")

		version += "+" + ".".join(metadata)

	# Regex from https://semver.org#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string
	if semver and not re.match(r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$", version):
		raise Exception(f"{version} is not a valid Semantic Versioning 2.0 string")

	return version

if __name__ == "__main__":
	_PARSER = argparse.ArgumentParser()
	_PARSER.add_argument("--prefix", default = None, help = "the prefix version tags have")
	_PARSER.add_argument("--semver", action = "store_true", help = "enforce Semantic Versioning 2.0")
	_ARGS = _PARSER.parse_args()
	print(get_version(prefix = _ARGS.prefix, semver = _ARGS.semver))