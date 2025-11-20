datafile = "./input_day1.txt"
elf_calories = []

with open(datafile, 'r') as file:
    data_per_elf = file.read().split("\n\n")

calories_per_elf = []
for data in data_per_elf:
    calories_per_elf.append(sum([int(x) for x in data.split("\n")]))

calories_per_elf.sort()

print(sum(calories_per_elf[-3:]))

