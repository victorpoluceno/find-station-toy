#!/bin/sh
make run JSON_STATIONS='[[0, 0, 10], [20, 20, 5], [10, 0, 12]]' JSON_POINT='[0, 0]'
make run JSON_STATIONS='[[0, 0, 10], [20, 20, 5], [10, 0, 12]]' JSON_POINT='[100, 100]'
make run JSON_STATIONS='[[0, 0, 10], [20, 20, 5], [10, 0, 12]]' JSON_POINT='[15, 10]'
make run JSON_STATIONS='[[0, 0, 10], [20, 20, 5], [10, 0, 12]]' JSON_POINT='[18, 18]'
