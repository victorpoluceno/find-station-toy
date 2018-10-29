import json
import math
import functools
from typing import Tuple, List, Iterable, Optional, NamedTuple


Power = float
Reach = float
Distance = float


class Point(NamedTuple):
    x: int
    y: int


class Device(NamedTuple):
    point: Point


class Station(NamedTuple):
    point: Point
    reach: float


class StationPower(NamedTuple):
    station: Station
    power: Power = 0


Stations = List[Station]


def find_most_suitable_station(stations: Stations, device: Device) \
        -> Optional[StationPower]:
    def compare(best_so_far: StationPower, candidate: StationPower) \
            -> StationPower:
        return candidate if candidate.power > best_so_far.power \
            else best_so_far

    station = functools.reduce(compare, enrich_stations_with_power(
        stations, device), StationPower(Station(Point(0, 0), 0)))
    return station if station.power > 0 else None


def enrich_stations_with_power(stations: Stations, device: Device) \
        -> Iterable[StationPower]:
    return map(lambda station: StationPower(
               station, station_power_to_device(station.reach,
                                                distance_to_station(
                                                    station.point,
                                                    device.point))), stations)


def station_power_to_device(reach: Reach, distance: Distance) -> Power:
    return 0.0 if distance > reach else (reach - distance)**2


def distance_to_station(station: Point, device: Point) -> Distance:
    return math.hypot(station.x - device.x,
                      station.y - device.y)
