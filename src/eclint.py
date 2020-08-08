"""Lint files not ignored by git against editorconfig."""

import subprocess
import checks

# Uses https://github.com/editorconfig-checker/editorconfig-checker
def run_eclint() -> None:
	"""
	Ensure all files not ignored by git respect editorconfig.

	:raise subprocess.CalledProcessError: A file does not respect editorconfig.
	:raise AssertionError: The current working directory is not the root of a git repository.
	"""
	checks.assert_is_root()

	untracked_files = subprocess.run(["git", "ls-files", "--others", "--exclude-standard", "--full-name"], capture_output = True, check = True, text = True).stdout.split("\n")
	untracked_files = [path.strip() for path in untracked_files if path.strip()]

	subprocess.run(["editorconfig-checker", "-ignore-defaults"], capture_output = False, check = True, text = True)

	for path in untracked_files:
		subprocess.run(["editorconfig-checker", "-ignore-defaults", path], capture_output = False, check = True, text = True)

if __name__ == "__main__":
	run_eclint()