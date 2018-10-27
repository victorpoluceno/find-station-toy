import json
import math
from typing import Tuple, List, Iterable, Optional, NamedTuple


Power = float
Reach = float
Distance = float


class Point(NamedTuple):
    x: int
    y: int


class Station(NamedTuple):
    point: Point
    reach: float
    power: float = 0.0


Stations = List[Station]


def stations_from_json(stations: str) -> List[Station]:
    return [Station(Point(station[0], station[1]), station[2])
            for station in json.loads(stations)]


def point_from_json(point: str) -> Point:
    return Point(*json.loads(point))


def find_most_suitable_station(stations: Stations, point: Point) \
        -> Optional[Station]:
    suitable_station = None
    for station in enrich_stations_with_power(stations, point):
        if station.power == 0.0:
            continue

        if suitable_station is None:
            suitable_station = station
        else:
            if station.power > suitable_station.power:
                suitable_station = station

    return suitable_station


def enrich_stations_with_power(stations: Stations, point: Point) \
        -> Iterable[Station]:
    for station in stations:
        power = station_power(
            station.reach, distance_to_station(station.point, point))
        yield Station(station.point, station.reach, power)


def station_power(reach: Reach, distance: Distance) -> Power:
    if distance > reach:
        return 0.0

    return (reach - distance)**2


def distance_to_station(station: Point, device: Point) -> Distance:
    return math.hypot(station.x - device.x,
                      station.y - device.y)
