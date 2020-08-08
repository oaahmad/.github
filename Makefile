_TOOL_PATH=./src
_PYTHON_COMMAND:=$(shell type -p python3 || echo python)

# See this file for more commands
include ./src/config/Makefile

# Lint files not ignored by git against editorconfig
.PHONY: eclint
eclint: setup
	@${_PYTHON_COMMAND} "${_TOOL_PATH}/eclint.py"

# Test gitignore
.PHONY: test-gitignore
test-gitignore: setup
	@${_PYTHON_COMMAND} "${_TOOL_PATH}/test_gitignore.py"

# Test the formatting of git tags
.PHONY: test-tags
test-tags: setup
	@${_PYTHON_COMMAND} "${_TOOL_PATH}/test_tags.py" --prefix v --semver --no-metadata --labels 'alpha,beta,rc' --label-number

# Get the version of the current commit
.PHONY: version
version: setup
	@${_PYTHON_COMMAND} "${_TOOL_PATH}/version.py" --prefix v --semver

# Fetch and prune from origin (including tags)
.PHONY: fetch
fetch:
	git fetch --prune origin "+refs/tags/*:refs/tags/*"

# Setup the project, and check if requirements are installed (run after cloning)
setup:
	# Pull all submodules
	git submodule update --init --recursive
	@${_PYTHON_COMMAND} "${_TOOL_PATH}/setup.py" --include ./src/config/setup.py
	touch setup

# Setup the project even if "make setup" already ran (force "make setup" to run)
.PHONY: reset
reset:
	rm -f setup
	make setup

# Initialize the repository (run after changing config/)
.PHONY: init
init:
	${_PYTHON_COMMAND} "${_TOOL_PATH}/init_repo.py"
	make reset
	# Update each submodule to the latest commit
	git submodule update --remote --merge

# You shouldn't need this (this initializes and pushes the repository after it is created)
.PHONY: first-init
first-init:
	git commit -m 'Added initial submodules (make first-init)'
	git push
	git add .
	git commit -m 'Added initial files (make first-init)'
	git push