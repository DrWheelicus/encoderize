# Contributing to Encoderize

First off, thank you for considering contributing to Encoderize! It's people like you that make Encoderize such a great tool.

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report for Encoderize.

- **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/DrWheelicus/encoderize/issues).
- If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/DrWheelicus/encoderize/issues/new). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for Encoderize, including completely new features and minor improvements to existing functionality.

- **Perform a cursory search** to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- If you cannot find an existing issue that describes your enhancement, [open a new issue](https://github.com/DrWheelicus/encoderize/issues/new).
- Provide a **clear and descriptive title** and include as many details as possible about the enhancement, explaining **why** it would be useful.

### Pull Requests

1. Fork the repository and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. Ensure the test suite passes (`pytest`).
4. Make sure your code lints (`flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics`).
5. Issue that pull request!

## Style Guides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature").
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
- Limit the first line to 72 characters or less.
- Reference issues and pull requests liberally after the first line.
- Consider using [Conventional Commits](https://www.conventionalcommits.org/) for structured commit messages (e.g., `feat: Add new visualization type`).

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).
- Use `black` for code formatting.
- Use `flake8` for linting.

## Releasing (Maintainers)

Releases are automated via GitHub Actions. To create a new release:

1. **Update the version** in `encoderize/__init__.py`:
   ```python
   __version__ = "0.2.0"  # Use semantic versioning
   ```

2. **Commit the version bump**:
   ```bash
   git add encoderize/__init__.py
   git commit -m "chore: bump version to 0.2.0"
   git push
   ```

3. **Create and push a tag** (must match the version with a `v` prefix):
   ```bash
   git tag v0.2.0
   git push --tags
   ```

4. The release workflow will automatically:
   - Run tests to ensure everything passes
   - Build the package (sdist and wheel)
   - Publish to PyPI
   - Create a GitHub Release with auto-generated release notes

### First-Time Setup (PyPI Trusted Publishing)

Before the first automated release, a maintainer must configure trusted publishing on PyPI:

1. Go to https://pypi.org/manage/project/encoderize/settings/publishing/
2. Add a new publisher with:
   - Owner: `DrWheelicus`
   - Repository: `encoderize`
   - Workflow name: `release.yml`
   - Environment name: `Main Deployment`

## Any questions?

Feel free to reach out if you have questions about contributing. 