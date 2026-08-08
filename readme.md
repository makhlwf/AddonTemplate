# NVDA Add-on Template

This repository contains a basic template structure for NVDA add-on development, building, distribution, and localization.
For details about NVDA add-on development, please see the [NVDA Add-on Development Guide](https://github.com/nvdaaddons/DevGuide/wiki/NVDA-Add-on-Development-Guide).

## Documentation Structure

- **`help.md`**: User-facing documentation distributed with the add-on (compiled to `help.html`).
- **`README.md`**: Repository and developer documentation.

## Development & Building

### Requirements
- Python 3.10+ (Python 3.13 64-bit recommended)
- `uv` package manager or SCons

### Quick Start
1. Install dependencies:
   ```sh
   uv sync
   ```
2. Build the add-on:
   ```sh
   uv run scons
   ```
   The created `.nvda-addon` bundle will be placed in the repository root.

### Managing Documentation

1. Create or edit `help.md` in the root directory for your add-on's user documentation.
2. User documentation files for translated languages are placed into `addon/doc/<lang>/help.md`.
3. When built with SCons, `help.md` (or translated `help.md` files) are automatically compiled to `help.html` and bundled with the add-on manifest specifying `docFileName = help.html`.

## Code Quality & Linters

This project uses modern tools for code formatting, linting, and type checking:

* **Ruff**: Fast Python linter configured in `pyproject.toml` (`[tool.ruff]`).
* **Pyright**: Static type checker configured in `pyproject.toml` (`[tool.pyright]`).
* **prek**: Pre-commit hook runner configured in `prek.toml`. Run `uv run prek install` to set up git hooks, or `uv run prek run --all-files` to run checks manually.

## Translation Workflow

Documentation and interface strings are synchronized with Crowdin via `.github/workflows/crowdinL10n.yml`. See `docs/l10n/addonAuthors.md` for detailed instructions on authoring and managing translations.
