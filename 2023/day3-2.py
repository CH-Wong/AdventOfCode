import math

with open("input_day3.txt") as file:
    data = file.readlines()

symbol_locs = []
nums = []
num_locs = []

for rownum, row in enumerate(data):
    parsed_row = ""
    for char_pos, char in enumerate(row):
        if char == "\n":
            break
        elif not char.isnumeric() and char != ".":
            if char == "*":
                symbol_locs.append((rownum, char_pos))
            parsed_row += (".")
        else:
            parsed_row += char
    
    pos = 0
    for value in parsed_row.split("."):
        cur_num = ""
        start_ind = pos
        if value.isnumeric():
            nums.append(int(value))
            locs = [(rownum, pos + ind) for ind in range(len(value))]
            num_locs.append(locs)
            pos += len(value)
        pos += 1

adjacent_num_lists = []

for (sym_row, sym_col) in symbol_locs:
    cur_adjacent_nums = []
    for num_id , locs in enumerate(num_locs):
        for (num_row, num_col) in locs:
            if abs(num_row - sym_row) <= 1 and abs(num_col - sym_col) <= 1:
                cur_adjacent_nums.append(num_id)

    adjacent_num_lists.append(list(set(cur_adjacent_nums)))

gear_ratio = 0
for adjacent_nums in adjacent_num_lists:
    if len(adjacent_nums) == 2:
        gear_ratio += math.prod([nums[ind] for ind in adjacent_nums])

print(gear_ratio)