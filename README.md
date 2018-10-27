# Find Station

Service implementation of find the most suitable link station to a device.

## Requirements

You need Python 3.6+.

## Installing

Before anything you must setup the dev environment:

	make install

## Testing

To run the unit test suite:

	make test

## Type checking

Type annotations are used by default. You can type check the code base by running:

	make check

Note: the check is also executed before running the test suite.

## Running

You can easily run the application. The list of stations and the point are required arguments, encoded as JSON:

	make run JSON_STATIONS='[[[0, 0], 10]]' JSON_POINT='[0, 0]'
