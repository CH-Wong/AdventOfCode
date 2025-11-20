with open("input_day6.txt") as file:
    time, record = file.readlines()

time = int("".join(time.split(":")[1].split()))
record = int("".join(record.split(":")[1].split()))

print(time)
print(record)

def distance(t_total, t_charge):
    # s = v*t, v=t_charge
    return t_charge*(t_total - t_charge)

import math

t_m = math.floor((time - math.sqrt(time**2 - 4*record))/2)
t_p = math.floor((time + math.sqrt(time**2 - 4*record))/2)

print(t_m, t_p, t_p - t_m)