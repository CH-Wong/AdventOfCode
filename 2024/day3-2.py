import re

filename = "input_day3.txt"
with open(filename) as datafile:
    data = datafile.read()

pattern = "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, data)
print(matches)

do = True
remove_ind = []
dont_index = [m == "don't()" for m in matches]

remove_ind = []

for ind, m in enumerate(matches):
    if m == "do()":
        do = True
        remove_ind.append(ind)
    elif m == "don't()":
        do = False
        remove_ind.append(ind)
    elif do == False:
        remove_ind.append(ind)
    elif do == True:
        continue
    else:
        # ??? This shouldn't happen
        print("hello?")
        continue

matches = [m for ind, m in enumerate(matches) if ind not in remove_ind]


total = 0
for m in matches:
    num1, num2 = [int(x) for x  in re.findall("[0-9]+", m)]
    total += num1*num2

print(total)