# .github

Utilities and [community health files](https://docs.github.com/en/github/building-a-strong-community/creating-a-default-community-health-file) for my projects

<a href="https://github.com/oaahmad/.github/actions" title="Click to see actions">
	<img src="https://github.com/oaahmad/.github/workflows/test/badge.svg" alt="Displays the status of tests">
</a>
<a href="https://github.com/oaahmad/.github/actions" title="Click to see actions">
	<img src="https://github.com/oaahmad/.github/workflows/lint/badge.svg" alt="Displays the status of linters">
</a>

## About

This repository has files my projects can refer to. It also has utilities for making repositories, setting up cloned repositories, and performing basic tasks. This is for my own projects, and is tailored to my preferences.

## Use

1. Create a repository
2. Run:
```shell
git submodule add -f https://github.com/oaahmad/.github src/tools/git-tools
python3 src/tools/git-tools/src/init_repo.py
make first-init
```