<!---
Thank you for contributing to this NVDA add-on!

Before submitting your PR, please choose the template that best matches your contribution:
- Code Feature / Bug Fix: Use `.github/PULL_REQUEST_TEMPLATE/code_change.md`
- Translation / Localization: Use `.github/PULL_REQUEST_TEMPLATE/translation.md` (Note: Translations are managed via Crowdin)
- Documentation: Use `.github/PULL_REQUEST_TEMPLATE/documentation.md`
--->

## Summary & Motivation
<!-- Brief summary of what this pull request changes and why. Include link to issue if applicable. -->

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Refactoring / Maintenance
- [ ] CI / Build system / Infrastructure update
- [ ] Documentation update

## NVDA & Accessibility Testing
- [ ] **NVDA Version(s) Tested:** <!-- e.g., 2024.1, 2026.2, latest alpha -->
- [ ] **Speech Output:** Tested with NVDA speech synth and verified speech output accuracy.
- [ ] **Braille Output:** Tested with braille display / braille viewer (if applicable).
- [ ] **Keyboard Navigation:** Verified accessibility via keyboard shortcuts.

## Add-on Release Checklist
- [ ] **`buildVars.py`**: Updated `minimumNVDAVersion` or `lastTestedNVDAVersion` if required.
- [ ] **Changelog**: Added user-facing change summary to `changelog.md`.
- [ ] **Localization (`i18n`)**: New translatable strings are wrapped with `_()` and `scons pot` was run.

## Quality Assurance
- [ ] Code passes local linting & formatting checks (`ruff check`, `prek`).
- [ ] Automated tests pass (`pytest`).
