with open("input_day5.txt") as file:
    data = file.read()

chunks = data.split("\n\n")

mappings_list = []
for chunk in chunks[1:]:
    mappings = chunk.split("\n")[1:]

    mappings = [mapping.split() for mapping in mappings]
    for ind, mapping in enumerate(mappings):
        mappings[ind] = [int(val) for val in mappings[ind]]

    mappings_list.append(mappings)

_, seed_ranges = chunks[0].split(": ")
seed_ranges = [int(val) for val in seed_ranges.split()]

largest_seed = []
for s, r in zip(seed_ranges[::2], seed_ranges[1::2]):
    largest_seed.append(s+r)
largest_seed = max(largest_seed)

locations = []

import time
## invert the look-up, start by results instead, and then look if the seed is contained within the given seed ranges
mappings_list.reverse()
start = time.time()
for result in range (0,largest_seed):
    seed = result
    for mappings in mappings_list:
        for target, source, steps in mappings:
            if target <= seed <= target + steps:
                seed += - (target - source)
                break

    in_ranges = False
    for s, r in zip(seed_ranges[::2], seed_ranges[1::2]):
        if s <= seed <= s + r:
            in_ranges = True
            print("HELLOO")
            break
    if in_ranges == True:
        break
    
    if result%1000000 == 0:
        print(f"{result}/{largest_seed} = {100*result/largest_seed:.1f}%, {time.time() - start:.2f}s")

print(seed, result)