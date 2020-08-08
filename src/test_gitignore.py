"""Test gitignore."""

import subprocess
import checks

def test_gitignore() -> None:
	"""
	Ensure the gitignore file(s) work as expected.

	:raise Exception: A path is kept or ignored unexpectedly.
	:raise subprocess.CalledProcessError: Failed to check a path.
	:raise AssertionError: The current working directory is not the root of a git repository.
	"""
	checks.assert_is_root()

	special_characters = "._- 5"
	allowed_names = ["Ab"] + [f"very{character}long{character}name" for character in special_characters] + ["long" * 5]
	ignored_names = ["a", special_characters[1]] + [f"{character}{character}" for character in special_characters if character != "."] + [f"{character}name" for character in special_characters] + [f"name{character}" for character in special_characters]

	allowed_folders = allowed_names
	allowed_root_folders = [".github"]
	ignored_folders = ignored_names + ["log", "logs", "node_modules", "temp", "temporary", "tmp"]
	ignored_root_folders = ["data", "settings"]
	allowed_file_names = allowed_names
	allowed_files = [".editorconfig", "Makefile", ".gitignore", ".gitattributes"]
	allowed_root_files = [".mailmap"]
	ignored_files = ["name", "a.min.md", "package-lock.json"]
	allowed_extensions = ["md", "txt"]
	no_extension_paths = ["src/tools/hooks/"]

	allowed_files += [f"{name}.{allowed_extensions[0]}" for name in allowed_file_names] + [f"{allowed_file_names[0]}.{extension}" for extension in allowed_extensions[1:]]
	ignored_files += [f"{name}.blah" for name in allowed_names] + [f"{ignored_names[0]}.{extension}" for extension in allowed_extensions] + [f"{name}.{allowed_extensions[0]}" for name in ignored_names] + allowed_extensions
	allowed_paths = ["./", f"{allowed_folders[0]}/", f"{allowed_root_folders[0]}/{allowed_folders[1]}/{allowed_folders[2]}/"] + [f"{folder}/{folder}/{folder}/" for folder in allowed_folders] + [f"{folder}/" for folder in allowed_root_folders] + [f"{allowed_folders[0]}/{folder}/" for folder in ignored_root_folders]
	ignored_paths = [f"{allowed_folders[0]}/{allowed_folders[1]}/{ignored_folders[2]}/"] + [f"{ignored_folders[0]}/{allowed_folders[1]}/{allowed_folders[2]}/"] + [f"{allowed_folders[0]}/{folder}/" for folder in ignored_folders] + [f"{folder}/" for folder in ignored_root_folders]

	keep_paths = []
	ignore_paths = []

	for path in allowed_paths:
		for f in allowed_files:
			keep_paths.append(f"{path}{f}")

	for path in ignored_paths:
		for f in allowed_files:
			ignore_paths.append(f"{path}{f}")

	for path in allowed_paths:
		for f in ignored_files:
			ignore_paths.append(f"{path}{f}")

	for path in no_extension_paths:
		keep_paths.append(f"{path}name")

	for f in allowed_root_files:
		keep_paths.append(f)

	try:
		ignored = subprocess.run(["git", "check-ignore", "--no-index", *keep_paths, *ignore_paths], capture_output = True, check = True, text = True)
	except subprocess.CalledProcessError as e:
		if ignored.returncode != 1:
			raise e

	if ignored.stdout.strip() != "\n".join(ignore_paths):
		ignored = ignored.stdout.strip().split("\n")
		message = []

		for path in keep_paths:
			if path in ignored:
				message.append(f"{path} incorrectly ignored")

		for path in ignore_paths:
			if path not in ignored:
				message.append(f"{path} incorrectly kept")

		raise Exception("\n".join(message))

if __name__ == "__main__":
	test_gitignore()