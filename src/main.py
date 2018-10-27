from core import find_most_suitable_station, \
    stations_from_json, point_from_json

import click


@click.command()
@click.option(
    '--json_stations', help='List of stations in JSON, e.g: [[[0, 0], 10]]',
    required=True)
@click.option(
    '--json_point', help='Device point to search for in JSON, e.g: [0, 1]',
    required=True)
def main(json_stations: str, json_point: str) -> None:
    stations, point = stations_from_json(json_stations), \
        point_from_json(json_point)
    station = find_most_suitable_station(stations, point)
    if station is None:
        click.echo("No link station within reach for point x,y")
    else:
        click.echo(
            "Best link station for point %d,%d is %d,%d with power %0.2f" %
            (point.x, point.y, station.point.x, station.point.y,
             station.power))


if __name__ == '__main__':
    main()
