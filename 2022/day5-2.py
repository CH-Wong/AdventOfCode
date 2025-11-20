import math
import re

with open("input_day5_initial.txt") as datafile:
    initial_data = datafile.read().split("\n")

num_stacks = math.ceil(len(initial_data[0])/4)
stacks = [[] for stack in range(num_stacks)]

for row in initial_data:
    for index in range(num_stacks):
        crate = row[(index*4) + 1]
        if not crate == " ":
            stacks[index].append(crate)

with open("input_day5_operations.txt") as datafile:
    operations = datafile.read().split("\n")

operation_regex = "move (?P<occurence>[0-9]+) from (?P<source>[0-9]+) to (?P<target>[0-9]+)"
for operation in operations:
    occurence, source, target = re.match(operation_regex, operation).groupdict().values()
    occurence = int(occurence)
    source = int(source)
    target = int(target)

    crates = stacks[source-1][0:occurence]
    stacks[source-1] = stacks[source-1][occurence:]
    stacks[target-1] = crates + stacks[target-1] 

top_crates = ""
for stack in stacks:
    top_crates += stack[0]

print(top_crates)