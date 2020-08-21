# Suggested Practices

These are suggested practices for my projects. These practices should not be pushed on projects with existing standards, or conventions.

## Directories

Use this directory structure:
* build/ - Output when building from source
* data/ - Generated data
	- logs/ - Logs generated
	- temp/ - Temporary files/folders generated
* settings/ - User settings
* src/ - Source code
	- config/ - Project configuration files (not user settings)
	- resources/ - Resources needed
		- files/
		- fonts/
		- images/
		- videos/
	- tests/ - Tests
		- integration/ - Test larger units of interacting code
		- system/ - Test the built software as a whole
		- unit/ - Test small units of code
	- tools/ - Utilities
* LICENSE.md
* README.md

## Files

Prefer markdown for documentation. Prefer [TOML](https://toml.io/en) for configuration files. Give files extensions (even shell scripts). Make file extensions lowercase.

Prefer:
* `.txt` for plain text
* `.md` for markdown
* `.sh` for shell scripts
* `.cpp` for C++

## License

**Disclaimer: The licenses mentioned here are merely suggestions. They are not actual licenses for actual works.**

Use an [Open Source Initiative](https://opensource.org) approved license for open source. Prefer [The MIT License (MIT)](https://opensource.org/licenses/MIT).

Only make a proprietary license with a lawyer's help. Consider that licenses themselves can have restrictions on their use (you may not be allowed to copy the license, or even parts of it).

## Accessibility

Consider accessibility from the start. Avoid only using color to differentiate UI elements/concepts. When color choices are arbitrary, avoid using colors that are hard for people with more common forms of color-blindness. Maintain good contrast. When possible, use the user's system settings to determine colors (eg. check if the user prefers dark themes, or high contrast themes). When possible, use the user's system settings to determine whether they prefer reduced motion (animation). Ensure the UI works well when font sizes change. Allow forms of navigation that are easier for visually impaired users, and users that have trouble using a mouse (eg. keyboard navigation/shortcuts). Indicate when a UI element has focus, especially if the element entered focus via keyboard. Avoid making mouse events the only way to see/do things (eg. also bind the actions to focus events).

## Colors

Consider [accessibility](#accessibility). Try [ColorBrewer](https://colorbrewer2.org), if appropriate. Try [this contrast checker](https://webaim.org/resources/contrastchecker).

## Localization

Consider localization from the start. Support [Unicode](https://home.unicode.org). If possible, have a separate repository for translations / language packs. Consider numbers, units, dates, and times for localization. Keep time zones in mind. Consider right-to-left, and vertical languages when designing UI.

## Security

Consider security from the start. Protect/encrypt stored data. Protect/encrypt transferred data. Protect/encrypt secrets. Hide user data. Block unsupported actions.

## Source Control

### Branches

Commit often. Use pull requests before merging into the main branch. Use squash merge (reduce the branch's history to a single commit). Make big changes in other branches, but try to break big changes into smaller pieces (so changes are merged to the main branch frequently). Merge the main branch into other branches often. Ultimately, all branches need to merge back into the main branch without it being a headache. Do not include a `development` branch. The main branch is the development branch.

### Tags

Use git tags to mark versions, and do not use tags for other purposes.

## Issue Labels

```
Help Wanted
Help wanted from community
#0e8a16

Status: Duplicate
Already exists
#ffffff

Status: Needs More Info
Needs more information
#000000

Status: Needs Review
Potentially resolved, but needs review
#cccccc

Status: Under Discussion
Needs to be discussed
#333333

Status: Won't Fix
Won't be worked on
#ffffff

Type: Bug
Something isn't working
#e99695

Type: Documentation
Improvements or additions to documentation
#d4c5f9

Type: Enhancement
Feature addition, change, or request
#bfd4f2

Type: Maintenance
Refactoring, tests, etc.
#fef2c0
```

## Planning

Prefer [UML](http://uml.org) for diagrams. Prefer UML class diagrams over [ERD](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) diagrams. When possible, use tools to generate diagrams.

Mock up user interfaces for big new features. Note any potential edge cases. Consider how different parts of the program will interact with each other.

## Command Line Interfaces

Support these options:
* `-v`, `--version` (print only the version number)
* `-h`, `--help` (print help)

## Tests and Contracts

Run all automated tests before each release. Also, manually test additions and changes before release. Test keyboard navigation. When writing tests, always make them fail first to make sure they are working. When appropriate, write performance tests.

Consider the following for unit tests: [unittest](https://docs.python.org/3/library/unittest.html), [JUnit](https://junit.org), [Google Test](https://github.com/google/googletest), [Jest](https://jestjs.io), [munit](https://github.com/massiveinteractive/MassiveUnit). For web projects, consider [Selenium](https://selenium.dev) for integration and system testing.

Consider the following for contracts: [this module](https://github.com/deadpixi/contracts), [Contracts for Java](https://github.com/nhatminhle/cofoja), [Boost Contracts](https://www.boost.org/doc/libs/1_71_0/libs/contract/doc/html/index.html), [Babel Contracts](https://github.com/codemix/babel-plugin-contracts), [HaxeContracts](https://github.com/ciscoheat/HaxeContracts).

## Web

Use [web components](https://developer.mozilla.org/en-US/docs/Web/Web_Components) ([custom elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements), [shadow DOM](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM), [HTML templates](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_templates_and_slots)). Use [sanitize.css](https://csstools.github.io/sanitize.css). Keep an eye out for FireFox support of [dialog](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog).

Minify and unify CSS files. Minify and unify JavaScript files with Google's [Closure Compiler](https://developers.google.com/closure/compiler/docs/gettingstarted_app), but keep an eye out on [WebAssembly](https://webassembly.org) progress (garbage collection, JavaScript compiler).

## General

When possible, support undoing actions. Use [garbage collection](https://hboehm.info/gc), or [smart pointers](https://www.boost.org/doc/libs/1_71_0/libs/smart_ptr/doc/html/smart_ptr.html). Use object-oriented programming (except maybe for small scripts that will not be used as libraries).