# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]
### Added
- Added `extract_from_text` utility.
- Added `fetch_text` script to text for a list of page titles.
- Feature extraction rule using revscoring extract.
- Gradient boosting config.
- Added Word Vectors feature lists.
- Added `mid_level_wp` to arguments.
- Added `fetch_page_wikiprojects` script to label pages with all wikiprojects.
- Parser code for generating mapping of mid-level topics to wikiprojects.
- Exception handling for request failures.
- Added requirement for revscoring v2.5.1
- Added requirement for mediawiki-utilities v0.4.18.
- Parser Tests.
- Release Criteria.

### Fixed
- Headings regex bug.

### Changed
- Escape angular brackets.
- Refactored logic for request processing.
- Use Pytest for testing.
- Dataset output file contains a date now.

### Removed
- mediawiki-utilities==0.4.18

## [0.1.1] - 2017-09-05
### Added
- Bootstrap code.
- WikiProjects Parsing Script.
