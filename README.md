# recommender-systems

[![Release](https://img.shields.io/github/v/release/nikolaos-mavromatis/recommender-systems)](https://img.shields.io/github/v/release/nikolaos-mavromatis/recommender-systems)
[![Build status](https://img.shields.io/github/actions/workflow/status/nikolaos-mavromatis/recommender-systems/main.yml?branch=main)](https://github.com/nikolaos-mavromatis/recommender-systems/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/nikolaos-mavromatis/recommender-systems/branch/main/graph/badge.svg)](https://codecov.io/gh/nikolaos-mavromatis/recommender-systems)
[![Commit activity](https://img.shields.io/github/commit-activity/m/nikolaos-mavromatis/recommender-systems)](https://img.shields.io/github/commit-activity/m/nikolaos-mavromatis/recommender-systems)
[![License](https://img.shields.io/github/license/nikolaos-mavromatis/recommender-systems)](https://img.shields.io/github/license/nikolaos-mavromatis/recommender-systems)

A collection of notebooks and scripts using various recommender system techniques.

- **Github repository**: <https://github.com/nikolaos-mavromatis/recommender-systems/>
- **Documentation** <https://nikolaos-mavromatis.github.io/recommender-systems/>

## Getting started with your project

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:nikolaos-mavromatis/recommender-systems.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/codecov/).

## Releasing a new version



---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).
