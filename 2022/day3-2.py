dictionary_input = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_dictionary = {letter: num+1 for num, letter in enumerate(dictionary_input)}

with open("input_day3.txt") as datafile:
    rucksacks = datafile.read().split("\n")

groups = []
group_data = []
for num, rucksack in enumerate(rucksacks):
    if num%3 == 0 and num!=0:
        groups.append(group_data)
        group_data = []
    
    group_data.append(rucksack)
    
total_priority = 0

for [rucksack1, rucksack2, rucksack3] in groups:
    common_item = list(set(rucksack1) & set(rucksack2) & set(rucksack3))[0]
    total_priority += alphabet_dictionary[common_item[0]]

print(total_priority)