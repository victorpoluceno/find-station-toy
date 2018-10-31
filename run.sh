#!/bin/sh
docker run find-station --json_stations '[[0, 0, 10], [20, 20, 5], [10, 0, 12]]' --json_point '[0, 0]'
docker run find-station --json_stations '[[0, 0, 10], [20, 20, 5], [10, 0, 12]]' --json_point '[100, 100]'
docker run find-station --json_stations '[[0, 0, 10], [20, 20, 5], [10, 0, 12]]' --json_point '[15, 10]'
docker run find-station --json_stations '[[0, 0, 10], [20, 20, 5], [10, 0, 12]]' --json_point '[18, 18]'
