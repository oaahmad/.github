"""Initialize the repository (run this after creating the repository, or after changing config/)."""

import gitignore, os, re, runpy, shutil, subprocess
import checks

_GENERATED_COMMENT = "# Note: This file may be regenerated (modify \"src/config/\" instead)\n\n"

def _make_gitignore() -> None:
	"""Make the gitignore file."""
	settings = runpy.run_path(os.path.join("src", "config", "gitignore.py"))
	allow_directories = gitignore.ALLOW_DIRECTORIES + settings.get("ALLOW_DIRECTORIES", [])
	ignore_directories = gitignore.IGNORE_DIRECTORIES + settings.get("IGNORE_DIRECTORIES", [])
	allow_extensions = gitignore.ALLOW_EXTENSIONS + settings.get("ALLOW_EXTENSIONS", [])
	allow_files = gitignore.ALLOW_FILES + settings.get("ALLOW_FILES", [])
	ignore_files = gitignore.IGNORE_FILES + settings.get("IGNORE_FILES", [])

	text = gitignore.TEXT.strip()
	extra = settings.get("TEXT", "").strip()

	if extra:
		text += "\n\n" + extra

	folder_pattern = settings.get("FOLDER_PATTERN", None)
	folder_pattern = folder_pattern if folder_pattern else gitignore.FOLDER_PATTERN
	file_pattern = settings.get("FILE_PATTERN", None)
	file_pattern = file_pattern if file_pattern else gitignore.FILE_PATTERN

	text %= {
		"folder_pattern": folder_pattern,
		"allow_directories": "\n".join([f"!{directory}/" for directory in allow_directories]),
		"ignore_directories": "\n".join([f"{directory}/" for directory in ignore_directories]),
		"allow_extensions": "\n".join([f"!{file_pattern}.{extension}" for extension in allow_extensions]),
		"allow_files": "\n".join([f"!{path}" for path in allow_files]),
		"ignore_files": "\n".join(ignore_files),
	}

	with open(".gitignore", "w") as f:
		f.write(_GENERATED_COMMENT)
		f.write(text)

def init_repo() -> None:
	"""
	Initialize the repository (run this after creating the repository, or after changing config/).

	:raise subprocess.CalledProcessError: A shell command failed.
	:raise AssertionError: The current working directory is not the root of a git repository.
	"""
	checks.assert_is_root()

	repo_name = os.path.basename(os.getcwd())

	if repo_name == ".github":
		_make_gitignore()
		return

	tool_path = os.path.join("src", "tools", "git-tools")

	if not os.path.isdir(tool_path):
		# Add the git-tools submodule
		subprocess.run(["git", "submodule", "add", "-f", "https://github.com/oaahmad/.github", tool_path], capture_output = False, check = True, text = True)

	# Initialize all submodules
	subprocess.run(["git", "submodule", "init"], capture_output = False, check = True, text = True)

	os.makedirs(os.path.join("src", "config"), exist_ok = True)
	config_path = os.path.join(tool_path, "src", "config")

	for entry in os.listdir(config_path):
		source = os.path.join(config_path, entry)
		target = os.path.join("src", "config", entry)

		if os.path.isfile(source) and not os.path.isfile(target):
			shutil.copy(source, target)

	with open(os.path.join("src", "config", "url.txt")) as f:
		url = f.read().strip()

	if not os.path.isfile("README.md"):
		with open(os.path.join(tool_path, "src", "resources", "README.md")) as source, open("README.md", "w") as target:
			target.write(source.read().replace("{{repo}}", repo_name).replace("{{url}}", url))

	with open(os.path.join(tool_path, "Makefile")) as source, open("Makefile", "w") as target:
		target.write(_GENERATED_COMMENT)
		target.write(re.sub(r"^\s*_TOOL_PATH\s*\=.*", "_TOOL_PATH=./src/tools/git-tools/src", source.read(), count = 1))

	filename = ".gitattributes"

	with open(os.path.join(tool_path, filename)) as source1, open(os.path.join("src", "config", filename)) as source2, open(filename, "w") as target:
		target.write(_GENERATED_COMMENT)
		target.write(source1.read())
		text = source2.read()

		if text:
			target.write("\n\n")
			target.write(text)

	settings = runpy.run_path(os.path.join("src", "config", "editorconfig.py"))
	ignore = settings.get("IGNORE", "")
	extra = settings.get("TEXT", "").strip()
	unset = ["indent_style", "indent_size", "end_of_line", "charset", "trim_trailing_whitespace", "insert_final_newline"]
	unset_lines = "\n".join([f"{line} = unset" for line in unset])

	with open(os.path.join(tool_path, ".editorconfig")) as f:
		text = f.read()

	if extra:
		text += "\n\n" + extra

	for glob in ignore:
		text += f"\n\n# Ignore\n[{glob}]\n{unset_lines}"

	with open(".editorconfig", "w") as f:
		f.write(_GENERATED_COMMENT)
		f.write(text)

	_make_gitignore()
	shutil.copytree(os.path.join(tool_path, "src", "tools", "hooks"), os.path.join("src", "tools", "hooks"), dirs_exist_ok = True)
	shutil.copytree(os.path.join(tool_path, ".github", "workflows"), os.path.join(".github", "workflows"), dirs_exist_ok = True)
	shutil.copytree(os.path.join(tool_path, ".github", "ISSUE_TEMPLATE"), os.path.join(".github", "ISSUE_TEMPLATE"), dirs_exist_ok = True)

	if os.path.isfile("setup"):
		os.remove("setup")

if __name__ == "__main__":
	init_repo()