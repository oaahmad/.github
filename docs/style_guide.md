# Code Style Guide

## General

Reduce code/logic inside class constructors. Avoid repeating code.

Explicitly specify parameter and return types (even if `None`/`void`), or use type hints when that is not possible.
```python
def some_function(some_parameter: str = "something", some_other_parameter: Optional[int] = None) -> None:
	pass
```

Use leading zeros for decimal/float numbers.
```css
div{
	something: 0.5;
}
```

Import from the built-in library first, then external libraries, then internal code. Otherwise, order imports alphabetically.
```python
import argparse, os, runpy, shutil, stat, subprocess
from typing import Optional
import checks
```

## Names

Use American English for code. Make names descriptive, but not more verbose than needed. Do not use unusual abbreviations to shorten names. Avoid negation in names (eg. "not", "no", "disallow", "prevent") unless you cannot reword it to have the same meaning (or you cannot practically rewrite the code to do the opposite).

Use `THIS_CASE` for global and class variables. Use `ThisCase` for types. Otherwise, use the same casing as the standard library for the language (for functions, methods, parameters, and local variables).

## Whitespace/Spacing

Follow the [editorconfig](https://editorconfig.org) file.

Do not use spacing to align things across lines (eg. operators).
```python
a = "a"
one = 1
something = "something"
```

Put one space around either side of boolean operators (including logical operators).
```javascript
something += somethingElse;
number1 += number2;
number3 = number1 + number2;
number4 = number1 / number2;

if (one && two || three){
	;
}
```

Put one space around each `=` when assigning values.
```python
def some_function(some_parameter = 1):
	pass

some_function(some_parameter = 2)
```

Do not put spaces inside brackets of any kind. Separate each item with one space after the comma. Separate key-value pairs with one space after the colon.
```python
a_list = [1, 2, 3]
a_dictionary = {"key": "value", "key2": "value2"}
function_call(argument1, argument2)
function_call()

def function_definition(argument1, argument2):
	pass
```

Do not put whitespace before the opening bracket for parameters or arguments.
```javascript
functionCall(1, 2, 3);

function someFunction(one, two, three){
	;
}

function(one, two, three){
	;
}
```

Put a space before the opening bracket for control flow statements. Put opening curly braces on the same line with no space. If a block depends on the previous block (eg. "else", "catch"), start it on the same line the previous block ends. Otherwise, do not start it on the same line. Put a space after each `;` in a loop header.
```javascript
function someFunction(){
	for (var i = 0; i < something.length; i++){
		if (something){
			;
		}
		if (somethingElse){
			;
		}
	}
}

function someOtherFunction(){
	if (something){
		try{
			;
		} catch (e){
			;
		}
	} else if (somethingElse){
		;
	}
}
```

Without curly braces, if a block depends on the previous block (eg. "else", "catch"), do not put any blank lines between those blocks.
```python
if something:
	pass
else:
	pass
```

Do not use more than one blank line to separate code. Immediately follow headers with content. Separate type, method, and function definitions with one blank line. Separate class variables from the first method by one blank line.
```python
class SomeClass(object):
	def some_method(self):
		for each in [1, 2, 3]:
			pass

	def some_other_method(self):
		pass

class SomeClass(object):
	CLASS_VARIABLE1 = None
	CLASS_VARIABLE2 = None

	def some_method(self):
		for each in [1, 2, 3]:
			pass

	def some_other_method(self):
		pass

class SomeClass(object):
	"""Some docstring"""
	def some_method(self):
		"""Some docstring"""
		for each in [1, 2, 3]:
			pass

class SomeClass(object):
	"""Some docstring"""
	CLASS_VARIABLE1 = None
	CLASS_VARIABLE2 = None
```

Do not hard wrap lines (rely on the code editor to make things look good). Only make an exception if the code would be especially hard to read on one line because of its complexity.
```python
complex_structure = {"key": [1, 2, 3], "key2": [4, 5, 6]}
chained_methods = something.one(a = 1, b = 2, c = 3).two(one = "one", two = "two", three = ["one", "two", "three"]).three()

text %= {
	"folder_pattern": folder_pattern,
	"allow_directories": "\n".join([f"!{directory}/" for directory in allow_directories]),
	"ignore_directories": "\n".join([f"{directory}/" for directory in ignore_directories]),
	"allow_extensions": "\n".join([f"!{file_pattern}.{extension}" for extension in allow_extensions]),
	"allow_files": "\n".join([f"!{path}" for path in allow_files]),
	"ignore_files": "\n".join(ignore_files),
}
```

## Comments

Other than doc comments / docstrings, only add comments when needed (aim to make code self-documenting first). However, add a comment if you need to clarify something that you cannot make clear with the code.

When giving credit with a comment, use the following format:
```
Taken from [link to source] [OR] Modified from [link to source]
License: [name of license] ([link to license, or path to local copy of license])
Date accessed: [full month name] [dd], [yyyy]
[Any other information required or recommended by the author/license]
```

Add a space after the start of a comment. Capitalize the start of a comment (unless there is a reason not to). Do not put inline comments next to code. Put comments above code.
```python
# Comment
some_function()
```

Besides doc comments, multiline comments should not have content on their first, and last lines.
```javascript
/*
A comment
with multiple lines
*/
```

Indent comments to the line they are for.
```python
def some_function():
	# Comment for someOtherFunction call
	someOtherFunction()
```

Never use strings as regular comments (only as docstrings).

## Code Documentation

Use doc comments / docstrings.

Use the following for code documentation: [JSDoc](https://jsdoc.app), [TSDoc](https://github.com/microsoft/tsdoc), [Dox](https://github.com/HaxeFoundation/dox/wiki), [reStructuredText](https://www.python.org/dev/peps/pep-0287) (for Python). Otherwise, use [javadoc](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/javadoc.html) if there is no clear convention for the language.

Use double quotes for docstrings. Use instructional terms in doc comments / docstrings (eg. "return" instead of "returns"). Use periods even if not using complete sentences.
```python
"""
Get the version of the current commit.

:usage: `python3 version.py --help`.
"""

def get_version(prefix: Optional[str] = None, semver: bool = False, default: str = "0.0.0") -> str:
	"""
	Return the version of the current commit using git tags.

	Put a longer description here, if needed.

	:deprecated: Use `coolNewFunction` instead
	:param prefix: Only consider tags with this prefix, and remove the prefix to get the version number.
	:param semver: Ensure the returned string is a Semantic Versioning 2.0 compliant string.
	:param default: Use this version if there is no version.
	:return: The version of the current commit. Include the full commit hash as metadata if it is not a release. Include a dirty indicator as metadata if there are uncommitted changes. For example, `1.0.0-beta.1+commit-5e94edf0845f6693683ab4e90b572d3a2967af1e.dirty`.
	:raise Exception: The version is not a Semantic Versioning 2.0 version (if `semver` is `True`).
	:raise subprocess.CalledProcessError: Failed to get tags, or a different shell command failed.
	:raise AssertionError: The current working directory is not the root of a git repository.
	"""
```

## Strings

Use double-quoted strings.
```python
"A string"
"A string with 'quotes'"
"A string with \"quotes\""
"A string with 'quotes' and other \"quotes\""
```

## HTML-Specific

Use [meta](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta) elements. Have at most one `h1` element per page. Only use generic elements like `div` or `span` when they are the only [appropriate options](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) (this helps accessibility, and SEO). Use buttons for actions and links as links. Use `p` for paragraphs. Break up text using different `p` elements (this helps screen readers separate sections of text). Button and link text should make sense out of context, and in the paragraph they are in (for screen readers). Give form inputs labels. Give images descriptive `alt` attributes describing what is in the image. If images are just for decoration, and can be skipped, provide an empty `alt` attribute. Use [kbd](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd) to represent keyboard input. Use [code](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code) for a line of code, and `code` wrapped in `pre` for multiple lines of code. Use [samp](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp) for sample output. Consider [skip links](https://a11yproject.com/posts/skip-nav-links). Use the [translate](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/translate) attribute to mark text that should not be translated by translation tools. Include JavaScript/script/code files at the bottom of the `body` element. Reduce JavaScript-generated HTML.

## CSS-Specific

Use [prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme), and [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion). Use [contain](https://developer.mozilla.org/en-US/docs/Web/CSS/contain) for elements that are changed/added/removed/hidden/duplicated after page load. Use [CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) (for values like numbers and colors). Reduce JavaScript-generated CSS.

## Markdown

```markdown
## Header 1

Content

## Header 2

More content

### Header 3

* Item
* Item 2
	- Sub item
	- Sub item 3
		- Sub item 4
* Item 3
```