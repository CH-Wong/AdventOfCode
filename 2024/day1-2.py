from collections import Counter

filename = "input_day1.txt"

with open(filename) as datafile:
    data = [int(x) for x in datafile.read().split()]

ids_left = data[::2]
ids_right = data[1::2]

count_right = Counter(ids_right)

similarity = 0
for l in ids_left:
    try: 
        similarity += l*count_right[l]
    except KeyError:
        continue

print(similarity)