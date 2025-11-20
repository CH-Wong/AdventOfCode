import re

filename = "input_day3.txt"
with open(filename) as datafile:
    data = datafile.read()


pattern = "mul\([0-9]+,[0-9]+\)"
matches = re.findall(pattern, data)


total = 0
for m in matches:
    num1, num2 = [int(x) for x  in re.findall("[0-9]+", m)]
    total += num1*num2

print(total)