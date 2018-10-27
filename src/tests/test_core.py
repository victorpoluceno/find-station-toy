from core import Point, Station, find_most_suitable_station, \
    distance_to_station, station_power, enrich_stations_with_power, \
    stations_from_json, point_from_json


def test_stations_from_json():
    assert stations_from_json("[[0, 0, 10]]") == [Station(Point(0, 0), 10)]


def test_point_from_json():
    assert point_from_json('[0, 0]') == Point(0, 0)


def test_find_most_suitable_station() -> None:
    stations = [Station(Point(0, 0), 10),
                Station(Point(20, 20), 5),
                Station(Point(10, 0), 12)]
    assert find_most_suitable_station(stations, Point(0, 0)) == Station(
        Point(0, 0), 10, 100.0)

    assert find_most_suitable_station(stations, Point(100, 100)) is None

    station = find_most_suitable_station(stations, Point(15, 10))
    assert station.point == Point(x=10, y=0)
    assert station.reach == 12
    assert round(station.power, 2) == 0.67

    station = find_most_suitable_station(stations, Point(18, 18))
    assert station.point == Point(x=20, y=20)
    assert station.reach == 5
    assert round(station.power, 2) == 4.72


def test_distance_to_station() -> None:
    assert distance_to_station(Point(0, 0), Point(0, 0)) == 0
    assert distance_to_station(Point(0, 0), Point(10, 0)) == 10.0
    assert distance_to_station(Point(10, 0), Point(0, 0)) == 10.0


def test_station_power() -> None:
    assert station_power(0, 10) == 0
    assert station_power(10, 10) == 0
    assert station_power(10, 5) == 25


def test_enrich_stations_with_power() -> None:
    stations = [Station(Point(0, 0), 10)]
    point = Point(0, 0)
    assert list(enrich_stations_with_power(stations, point)) == [
        Station(Point(0, 0), 10, 100.0)]
