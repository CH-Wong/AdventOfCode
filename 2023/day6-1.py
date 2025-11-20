with open("input_day6.txt") as file:
    times, records = file.readlines()

times = [int(t) for t in times.split(":")[1].split()]
records = [int(d) for d in records.split(":")[1].split()]

print(times)
print(records)

def distance(t_total, t_charge):
    # s = v*t, v=t_charge
    return t_charge*(t_total - t_charge)

success = []
for t, r in zip(times, records):
    curr_success = 0
    for t_charge in range(1, t):
        d = distance(t, t_charge)
        if d > r:
            curr_success += 1
    if curr_success > 0:
        success.append(curr_success)
print(success)
import math
print(math.prod(success))
    

