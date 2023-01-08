# Python Base Test

<!-- badges-begin -->
[![PyPI](https://img.shields.io/pypi/v/python-base-test.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/python-base-test.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/python-base-test)][pypi status]
[![License](https://img.shields.io/pypi/l/python-base-test)][license]

[![Read the documentation at https://python-base-test.readthedocs.io/](https://img.shields.io/readthedocs/python-base-test/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/DonalChilde/python-base-test/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/DonalChilde/python-base-test/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/python-base-test/
[read the docs]: https://python-base-test.readthedocs.io/
[tests]: https://github.com/DonalChilde/python-base-test/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/DonalChilde/python-base-test
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

<!-- badges-end -->

## Features

- TODO

## Requirements

- TODO

## Quickstart

You can install _Python Base Test_ via [pip] from [PyPI]:

```console
pip install python-base-test
```

## Usage

Please see the [documentation] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].


## Usage

Please see the [Command-line Reference] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Python Base Test_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Developer Setup

<!-- dev -->
### Individual commands

```bash
# From the project directory - 
python3 -m virtualenv ./.venv
source ./.venv/bin/activate
pip3 install -U pip, wheel
pip3 install -e .[dev,lint,doc,vscode,testing]
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/DonalChilde/python-base-test.git
```

### Convenient one liners

```bash
python3 -m virtualenv ./.venv && source ./.venv/bin/activate && export PIP_REQUIRE_VIRTUALENV=true && pip3 install -U pip && pip3 install -e .[dev,lint,doc,vscode,testing]
```

```bash
git init && git add . && git commit -m "initial commit"
```

```bash
git remote add origin https://github.com/DonalChilde/python-base-test.git
```
<!-- end-dev -->
## Credits

This project was generated from [DonalChilde]'s [cookiecutter-python-base] template, which was inspired by [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[DonalChilde]: https://github.com/DonalChilde
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[cookiecutter-python-base]: https://github.com/DonalChilde/cookiecutter-python-base
[file an issue]: https://github.com/DonalChilde/python-base-test/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/DonalChilde/python-base-test/blob/main/LICENSE
[contributor guide]: https://github.com/DonalChilde/python-base-test/blob/main/CONTRIBUTING
[documentation]: https://python-base-test.readthedocs.io/en/latest/
