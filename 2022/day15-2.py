import re
import numpy as np
import matplotlib.pyplot as plt
import time
from tqdm import tqdm

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


max_range = 4000001

out_of_range = set()
print("Processing sensors to get points to check...")
with tqdm(zip(sensors, distances), total=len(sensors)) as t:
    for [[sx, sy], d] in t:
        for y in range(sy - d - 1, sy + d + 2):
            k = abs(sy - y) - (d + 1)
            if 0 <= sx + k <= max_range and 0 <= y <= max_range:
                out_of_range.add((sx + k, y))

            if 0 <= sx - k <= max_range and 0 <= y <= max_range:   
                out_of_range.add((sx - k, y))

out_of_range = list(out_of_range)
print(f"{len(out_of_range)} points to check.\n\n")

sensors = np.array(list(map(list, sensors)))
start = time.time()

print("Checking points...")
with tqdm(out_of_range) as t:
    for [x, y] in t:
        if np.all(np.absolute(x - sensors[:,0]) + np.absolute(y - sensors[:,1]) > distances):
            print(x, y)
            print(x*4000000 + y)
            t.close()
            break
