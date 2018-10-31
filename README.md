# Find Station [![Build Status](https://travis-ci.org/victorpoluceno/find-station-toy.svg?branch=master)](https://travis-ci.org/victorpoluceno/find-station-toy)

Simple tool for finding the most suitable link station to a device.

## Architecture

The tool is composed of two main components, the `main` (CLI) and a `core` library. `main` is responsible for all the input and output of the tool. The `core` contains all the business logic implemented in a functional style.

As all side effects are constrained to the `main`, the `core` is easy to test and modify. The functional nature of the core and separation of concerns make the tool open for extension, for example making easy to add more interfaces (frontends) like a REST API.

## Usage

### Requirements

The minimal requirement for running this app is to have a Docker daemon running.

### Running

You can easily run the application. The list of stations and the point are required arguments, encoded as JSON:

	docker run find-station --json_stations '[[0, 0, 10]]' --json_point '[0, 0]'

### Demo

For a demonstration of this tool, there is a `run.sh` that will execute many searches and show the results.

## Developing

### Requirements

You need Python 3.6+.

### Installing

Before anything you must setup the dev environment:

	make install

### Testing

To run the unit test suite:

	make test

### Running (without Docker)

You can easily run the application. The list of stations and the point are required arguments, encoded as JSON:

	make run JSON_STATIONS='[[0, 0, 10]]' JSON_POINT='[0, 0]'

### Type checking

Type annotations are used by default. You can type check the code base by running:

	make check

Note: the check is also executed before running the test suite.

### Linting and style

There is a `.editorconfig` file available and a `.flake8`. You should use EditorConfig and flake8 in your editor of choice.