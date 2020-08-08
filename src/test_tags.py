"""
Test the formatting of git tags.

:usage: `python3 test_tags.py --help`.
"""

import argparse, re, subprocess
from typing import Optional, Iterable
import checks

def test_tags(prefix: Optional[str] = None, semver: bool = False, no_metadata: bool = False, labels: Optional[Iterable[str]] = None, label_number: bool = False) -> None:
	"""
	Ensure all git tags are formatted correctly.

	:param prefix: Ensure tags have this prefix.
	:param semver: Ensure tags are Semantic Versioning 2.0 compliant strings.
	:param no_metadata: Ensure tags do not have metadata (assume metadata is added as in Semantic Versioning 2.0).
	:param labels: Only allow these pre-release labels (ignored if semver is `False`).
	:param label_number: Ensure tags with labels have associated numbers (ignored if semver is `False`).
	:raise Exception: A tag is invalid.
	:raise subprocess.CalledProcessError: Failed to get tags.
	"""
	checks.assert_is_root()

	labels = list(labels)

	if prefix is None:
		prefix = ""

	tags = subprocess.run(["git", "tag", "--list"], capture_output = True, check = True, text = True).stdout.split("\n")
	tags = [tag.strip() for tag in tags if tag.strip()]

	if not tags:
		return

	for tag in tags:
		if not tag.startswith(prefix):
			raise Exception(f"{tag} does not start with {prefix}")

		if semver:
			tag = tag.lstrip(prefix)

			# Regex from https://semver.org#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string
			match = re.match(r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$", tag)

			if not match:
				raise Exception(f"{tag} is not a valid Semantic Versioning 2.0 string")

			if labels:
				label = match.group("prerelease")

				if label:
					if label_number and "." not in label:
						raise Exception(f"{tag} has a label without a number")

					label = label.split(".")[0]

					if label not in labels:
						raise Exception(f"{tag} has the invalid label {label.split('.')[0]}")

		if no_metadata and "+" in tag:
			raise Exception(f"{tag} has metadata")

if __name__ == "__main__":
	_PARSER = argparse.ArgumentParser()
	_PARSER.add_argument("--prefix", default = None, help = "the prefix version tags have")
	_PARSER.add_argument("--semver", action = "store_true", help = "enforce Semantic Versioning 2.0")
	_PARSER.add_argument("--no-metadata", action = "store_true", help = "disallow metadata")
	_PARSER.add_argument("--labels", default = "", help = "only allow these labels (comma-separated)")
	_PARSER.add_argument("--label-number", action = "store_true", help = "labels must have numbers")
	_ARGS = _PARSER.parse_args()
	_LABELS = _ARGS.labels.split(",")
	test_tags(prefix = _ARGS.prefix, semver = _ARGS.semver, no_metadata = _ARGS.no_metadata, labels = [label for label in _LABELS if label], label_number = _ARGS.label_number)