# This is included in the root Makefile (see that file for more commands)

# Run all tests
.PHONY: test
test: version test-gitignore test-tags
	@echo '✓ test success'

# Run all linters
.PHONY: lint
lint: eclint
	@echo '✓ lint success'

# Called by the pre-push hook
.PHONY: pre-push
pre-push: lint test