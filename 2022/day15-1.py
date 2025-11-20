import re
import numpy as np
import matplotlib.pyplot as plt

def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) 

with open("input_day15.txt") as datafile:
    sensordata = datafile.read().strip().split("\n")

sensors = []
beacons = []
distances = []

regex = "Sensor at x=(?P<sensor_x>-?\d+), y=(?P<sensor_y>-?\d+): closest beacon is at x=(?P<beacon_x>-?\d+), y=(?P<beacon_y>-?\d+)"
for item in sensordata:
    sensor_x, sensor_y, beacon_x, beacon_y = re.match(regex, item).groupdict().values()
    sensor = (int(sensor_x), int(sensor_y))
    beacon = (int(beacon_x), int(beacon_y))

    beacons.append(beacon)
    sensors.append(sensor)
    distances.append(distance(sensor, beacon))

occupied = set()
target_row = 2000000
for [sx, sy], d in zip(sensors, distances):
    if abs(sy - target_row) <= d:
        for i in range(d - abs(sy - target_row) + 1):
            occupied.add((sx + i, target_row))
            occupied.add((sx - i, target_row))

for pos in beacons:
    if pos in occupied:
        occupied.remove(pos)


print(len(occupied))

