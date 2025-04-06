# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-04-06

### Added
- Initial project setup with Hugo
- Integrated Terminal theme via git submodule
- Created basic content structure with sample post
- Set up GitHub repository (https://github.com/gahoccode/testing-hugo-12)
- Configured GitHub Pages deployment via gh-pages branch

### Changed
- Replaced `paginate = 5` with the new `[pagination]` section and `pagerSize = 5` parameter in hugo.toml
- Modified theme configuration in hugo.toml to use the Terminal theme

### Fixed
- Resolved Hugo build error: "site config key paginate was deprecated in Hugo v0.128.0"
- Fixed content structure to match Terminal theme requirements by adding `content/posts` directory

### Deployed
- Website deployed to GitHub Pages
- Main branch contains source code
- gh-pages branch contains the built static site
