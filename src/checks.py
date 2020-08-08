"""Check various conditions."""

import os, subprocess

def assert_is_root() -> None:
	"""
	Ensure the current working directory is the root of a git repository.

	:raise AssertionError: The current working directory is not the root of a git repository.
	:raise subprocess.CalledProcessError: Failed to get the root of the git repository.
	"""
	assert os.path.samefile(os.getcwd(), subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output = True, check = True, text = True).stdout.strip()), "You must run this from the root directory of the repository"

def assert_branch_exists() -> None:
	"""
	Ensure any git branch exists.

	:raise AssertionError: No branches exist.
	:raise subprocess.CalledProcessError: Failed to check for branches.
	"""
	assert subprocess.run(["git", "branch", "--list"], capture_output = True, check = True, text = True).stdout.strip(), "A branch must exist (make a commit)"