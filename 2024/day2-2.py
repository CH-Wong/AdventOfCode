filename = "input_day2.txt"

data = []
with open(filename) as datafile:
    for line in datafile.readlines():
        data.append([int(x) for x in line.split()])

n_safe = 0
for report in data:
    for ind in range(len(report)):
        pruned_report = report.copy()
        del pruned_report[ind]
        
        diff = [y - x for x,y in zip(pruned_report[:-1], pruned_report[1:])]
        if all([1 <= abs(x) <= 3 and (x > 0 or x < 0) for x in diff]) and (all([x > 0 for x in diff]) or all([x < 0 for x in diff])):   
            n_safe += 1
            break
        else:
            continue

print(f"Number of reports: {len(data)}")
print(f"Safe reports: {n_safe}")
