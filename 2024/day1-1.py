filename = "input_day1.txt"

with open(filename) as datafile:
    data = [int(x) for x in datafile.read().split()]

ids_left = data[::2]
ids_right = data[1::2]

dist = [abs(l-r) for l,r in zip(sorted(ids_left), sorted(ids_right))]

print(sum(dist))
