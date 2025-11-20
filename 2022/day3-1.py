dictionary_input = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_dictionary = {letter: num+1 for num, letter in enumerate(dictionary_input)}

with open("input_day3.txt") as datafile:
    rucksacks = datafile.readlines()

total_priority = 0
for rucksack in rucksacks:
    compartment1 = rucksack[0:int(len(rucksack)/2)]
    compartment2 = rucksack[int(len(rucksack)/2):-1]
    common_item = list(set(compartment1) & set(compartment2))
    total_priority += alphabet_dictionary[common_item[0]]

print(total_priority)