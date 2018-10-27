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

## Example

This shows a example of searching fro multiple points:

```
➜  find-station git:(master) ✗ sh run.sh
venv/bin/mypy --strict src/.
PYTHONPATH=src venv/bin/python src/main.py --json_stations '[[0, 0, 10], [20, 20, 5], [10, 0, 12]]' --json_point '[0, 0]'
Best link station for point 0,0 is 0,0 with power 100.00
venv/bin/mypy --strict src/.
PYTHONPATH=src venv/bin/python src/main.py --json_stations '[[0, 0, 10], [20, 20, 5], [10, 0, 12]]' --json_point '[100, 100]'
No link station within reach for point 100,100
venv/bin/mypy --strict src/.
PYTHONPATH=src venv/bin/python src/main.py --json_stations '[[0, 0, 10], [20, 20, 5], [10, 0, 12]]' --json_point '[15, 10]'
Best link station for point 15,10 is 10,0 with power 0.67
venv/bin/mypy --strict src/.
PYTHONPATH=src venv/bin/python src/main.py --json_stations '[[0, 0, 10], [20, 20, 5], [10, 0, 12]]' --json_point '[18, 18]'
Best link station for point 18,18 is 20,20 with power 4.72
```