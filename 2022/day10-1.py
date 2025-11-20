with open("input_day10.txt") as datafile:
    operations = datafile.read().strip().split("\n")

x = 1
x_hist = []

for operation in operations:
    if operation == "noop":
        x_hist.append(x)

    elif "addx" in operation:
        value = int(operation.split(" ")[1])
        x_hist.append(x)
        x_hist.append(x)
        x += value

cycles_of_interest = [20, 60, 100, 140, 180, 220]

signal_strengths = []
for cycle in cycles_of_interest:
    signal_strengths.append(cycle*x_hist[cycle-1])

print(sum(signal_strengths))