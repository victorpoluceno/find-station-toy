import json
from typing import List

import click

from core import Station, Point, Device, find_most_suitable_station


def stations_from_json(stations: str) -> List[Station]:
    return [Station(Point(station[0], station[1]), station[2])
            for station in json.loads(stations)]


def device_from_json(point: str) -> Device:
    return Device(Point(*json.loads(point)))


@click.command()
@click.option(
    '--json_stations', help='List of stations in JSON, e.g: [[0, 0, 10]]',
    required=True)
@click.option(
    '--json_point', help='Device point to search for in JSON, e.g: [0, 1]',
    required=True)
def main(json_stations: str, json_point: str) -> None:
    stations, device = stations_from_json(json_stations), \
        device_from_json(json_point)
    station_power = find_most_suitable_station(stations, device)
    if station_power is None:
        click.echo("No link station within reach for point %d,%d" %
                   (device.point.x, device.point.y))
    else:
        click.echo(
            "Best link station for point %d,%d is %d,%d with power %0.2f" %
            (device.point.x, device.point.y, station_power.station.point.x,
             station_power.station.point.y, station_power.power))


if __name__ == '__main__':
    main()
