"""
Setup the project, and check if requirements are installed (run this after cloning the repository).

:usage: `python3 setup.py --help`.
"""

import argparse, os, runpy, shutil, stat, subprocess
from typing import Optional
import checks

def setup(include: Optional[str] = None) -> None:
	"""
	Setup the project, and check if requirements are installed (run this after cloning the repository).

	:param include: The path to an additional setup file to include.
	:raise Exception: A required shell command is missing.
	:raise subprocess.CalledProcessError: A shell command failed.
	:raise AssertionError: The current working directory is not the root of a git repository.
	"""
	checks.assert_is_root()

	required_commands = ["git", "make", "python", "pip"]
	required_paths = []
	commands = []

	if include:
		imported = runpy.run_path(include)
		required_commands += imported.get("REQUIRED_COMMANDS", [])
		required_paths += imported.get("REQUIRED_PATHS", [])
		commands += imported.get("COMMANDS", [])

	for command in required_commands:
		if shutil.which(command) is None:
			raise Exception(f"The {command} command is required")

	for path in required_paths:
		os.makedirs(path.replace("/", os.sep), exist_ok = True)

	for command in commands:
		subprocess.run(command, capture_output = False, check = True, text = True)

	target = os.path.join(".git", "hooks")
	shutil.copytree(os.path.join("src", "tools", "hooks"), target, dirs_exist_ok = True)

	for entry in os.listdir(target):
		path = os.path.join(target, entry)

		if os.path.isfile(path):
			st = os.stat(path)
			os.chmod(path, st.st_mode | stat.S_IEXEC)

	if include and "setup" in imported:
		imported["setup"]()

if __name__ == "__main__":
	_PARSER = argparse.ArgumentParser()
	_PARSER.add_argument("--include", default = None, help = "path to the additional setup file")
	_ARGS = _PARSER.parse_args()
	setup(include = _ARGS.include)