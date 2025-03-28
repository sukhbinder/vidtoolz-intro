# vidtoolz-intro

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-intro.svg)](https://pypi.org/project/vidtoolz-intro/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-intro?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-intro/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-intro/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-intro/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-intro/blob/main/LICENSE)

Create intro video from a series of videos

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-intro
```
## Usage

type ``vid intro --help`` to get help



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-intro
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
