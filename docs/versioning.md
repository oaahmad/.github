# Versioning Standard

[Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)

Version numbers increase as follows:
* Major version: breaking changes
* Minor version: new features, significant changes, functionality marked as deprecated
* Patch version: minor implementation changes, bug fixes

Before removing functionality, there will be a minor release where it is marked as deprecated.

## Exceptions

If there is no API, API-related rules do not apply, or apply in a way that is more appropriate.

## Details

The following labels are used:
* `alpha`
	- Ready for internal testing
	- Make anticipated changes now
* `beta`
	- Ready for public testing
	- Minimize feature additions
	- Make anticipated changes before the release candidate
* `rc`
	- Feature-locked
	- Minimize changes, but fix bugs
	- Documentation may change

Final releases do not have a label. Labels always have a number (eg. `1.0.0-beta.1`).

Commit metadata (if different from the release), and a dirty flag will be added as needed (eg. `1.0.0-beta.1+commit-5e94edf0845f6693683ab4e90b572d3a2967af1e.dirty`). Users should avoid builds with this metadata.

The following are considered breaking changes:
* Changing or removing keyboard shortcuts
* Removing functionality
* Removing parameters for functionality
* Changing the default values of parameters
* Removing settings
* Changing default values for settings