# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-04-06

### Changed
- Replaced `paginate = 5` with the new `[pagination]` section and `pagerSize = 5` parameter in hugo.toml
- Modified theme configuration in hugo.toml to use the Terminal theme

### Fixed
- Resolved Hugo build error: "site config key paginate was deprecated in Hugo v0.128.0"
- Fixed content structure to match Terminal theme requirements by adding `content/posts` directory

## [0.1.1] - 2025-04-07

### Fixed
- Updated `baseurl` from "/" to "https://gahoccode.github.io/testing-hugo-12/" to fix missing CSS styling on GitHub Pages
