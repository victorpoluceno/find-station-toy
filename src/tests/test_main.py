from main import stations_from_json, device_from_json
from core import Station, Point, Device


def test_stations_from_json():
    assert stations_from_json("[[0, 0, 10]]") == [Station(Point(0, 0), 10)]


def test_point_from_json():
    assert device_from_json('[0, 0]') == Device(Point(0, 0))
