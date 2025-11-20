with open("input_day4.txt") as datafile:
    data = datafile.read()

num_overlap = 0
for pair in data.split("\n"):
    [set1, set2] = pair.split(",")
    [min1, max1] = set1.split("-")
    [min2, max2] = set2.split("-")

    if (int(min1) <= int(min2) and int(max1)) >= int(max2) or (int(min2) <= int(min1) and int(max2) >= int(max1)):
        num_overlap += 1

print(num_overlap)