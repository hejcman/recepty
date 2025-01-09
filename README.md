# Python Template

This template serves as the basis of my Python projects.
This template repository was created to unify coding styles and conventions for new projects.

## Using the template

To use the template, you should update it to fit your project:

1. Use the `rename_package.sh` script to rename the source code paths: ```bash rename_package.sh <YOUR_PACKAGE_NAME>```
2. Update the information inside `[project]` within the `pyproject.toml` file, such as the project name, the project author, the version, etc.

Further changes can be appropriate for your project, such as modifying the options for all the integrated tools.

### Template dependencies

This template integrates the following tools:

- Black for [code formatting](#code-formatting).
- Sphinx for [documentation](#documentation).
- PyTest for [testing](#testing).
- Ruff, Pylint, and MyPy for [linting and code checking](#linting-and-type-checking).

All these tools are also integrated in the preconfigured [pre-commit hooks](#pre-commit).

## Pre-commit

Pre-commit is a framework for managing and maintaining multi-language pre-commit hooks.
It works by running a set of scripts defined in `.pre-commit-config.yml`

## Code formatting

Code formatting is done using [Black](https://github.com/psf/black).
Black is an opinionated formatted with minimal configuration options, which results in more consistent code between projects.
It can be run manually by executing `black .` in the root of the projects.
However, formatting is done automatically using the included pre-commit hooks.

## Linting and Type Checking

For linting, [Ruff](https://beta.ruff.rs/docs/) and [PyLint](https://pylint.org/) are used.
Ruff is a tool written in Rust and implements many linting rules from existing tools (flake8, isort, ...) from scratch.
Ruff can therefore be used as a [drop in replacement for Flake8](https://beta.ruff.rs/docs/faq/#how-does-ruff-compare-to-flake8).
However, PyLint still offers [some features beyond the scope of Ruff](https://beta.ruff.rs/docs/faq/#how-does-ruff-compare-to-pylint), and is therefore used in tandem with Ruff.

Type checking is implemented with [MyPy](https://mypy.readthedocs.io/en/stable/).

## Documentation

The template is preconfigured to use [Sphinx](https://www.sphinx-doc.org/en/master/) for documentation.
Sphinx is the de-facto default tool for generating Python documentation.

### Using MkDocs

A good alternative to Sphinx is [MkDocs](https://www.mkdocs.org/), especially when paired with the [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) theme and the [mkdocstrings](https://mkdocstrings.github.io/) plugin.
This documentation framework is used in multiple large-scale projects such as [FastAPI](https://fastapi.tiangolo.com/) and [PyDantic](https://docs.pydantic.dev/).

Contrary to Sphinx, MkDocs doesn't import the documented source code, and instead only statically parses it.
This means that MkDocs tends to be much faster and less problematic for complext projects, where their importing can pose an issue.
Furthermore, MkDocs uses markdown instead of the more obscure reStructured text.
However, in many instances, Sphinx is still better. Make sure to use the best documentation framework for your project type.

## Testing

TODO

## Integrating with CI/CD

TODO

### GitLab CI

TODO

### GitHub Actions

TODO
