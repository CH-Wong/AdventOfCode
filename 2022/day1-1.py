datafile = "./input_day1.txt"
elf_calories = []

with open(datafile, 'r') as file:
    data_per_elf = file.read().split("\n\n")


calories_per_elf = []
for data in data_per_elf:
    calories_per_elf.append(sum([int(value) for value in data.split("\n")]))


print(max(calories_per_elf))
