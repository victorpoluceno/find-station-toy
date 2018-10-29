from core import Point, Station, StationPower, Device, \
    find_most_suitable_station, distance_to_station, \
    station_power_to_device, enrich_stations_with_power, \
    stations_from_json, device_from_json


def test_stations_from_json():
    assert stations_from_json("[[0, 0, 10]]") == [Station(Point(0, 0), 10)]


def test_point_from_json():
    assert device_from_json('[0, 0]') == Device(Point(0, 0))


def test_find_most_suitable_station() -> None:
    stations = [Station(Point(0, 0), 10),
                Station(Point(20, 20), 5),
                Station(Point(10, 0), 12)]
    assert find_most_suitable_station(stations, Device(Point(0, 0))) == \
        StationPower(Station(Point(0, 0), 10), 100.0)

    assert find_most_suitable_station(
        stations, Device(Point(100, 100))) is None

    station, power = find_most_suitable_station(
        stations, Device(Point(15, 10)))
    assert station.point == Point(x=10, y=0)
    assert station.reach == 12
    assert round(power, 2) == 0.67

    station, power = find_most_suitable_station(
        stations, Device(Point(18, 18)))
    assert station.point == Point(x=20, y=20)
    assert station.reach == 5
    assert round(power, 2) == 4.72


def test_distance_to_station() -> None:
    assert distance_to_station(Point(0, 0), Point(0, 0)) == 0
    assert distance_to_station(Point(0, 0), Point(10, 0)) == 10.0
    assert distance_to_station(Point(10, 0), Point(0, 0)) == 10.0


def test_station_power_to_device() -> None:
    assert station_power_to_device(0, 10) == 0
    assert station_power_to_device(10, 10) == 0
    assert station_power_to_device(10, 5) == 25


def test_enrich_stations_with_power() -> None:
    stations = [Station(Point(0, 0), 10)]
    device = Device(Point(0, 0))
    assert list(enrich_stations_with_power(stations, device)) == [
        StationPower(Station(Point(0, 0), 10), 100.0)]
