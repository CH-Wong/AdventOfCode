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

print("----------------------------------------")
line = ""
for cycle, x_val in enumerate(x_hist):
    pointer = (cycle)%40

    if x_val - 1 <= pointer <= x_val + 1:
        line += "#"

    else:
        line += " "

    if pointer == 39:
        print(line)
        line = ""
print("----------------------------------------")
