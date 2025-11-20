filename = "input_day2.txt"

data = []
with open(filename) as datafile:
    for line in datafile.readlines():
        data.append([int(x) for x in line.split()])

n_safe = 0
for report in data:
    diff = [y - x for x,y in zip(report[:-1], report[1:])]
    print(report, diff)
    if all([1 <= abs(x) <= 3 and (x > 0 or x < 0) for x in diff]) and (all([x > 0 for x in diff]) or all([x < 0 for x in diff])):
        n_safe += 1
        print("safe")

print(f"Number of reports: {len(data)}")
print(f"Safe reports: {n_safe}")
