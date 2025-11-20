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
            pos += len(value) + 1

        else:
            pos+=1

    
count_num = [False for i in range(len(nums))]
for num_id , locs in enumerate(num_locs):
    for (num_row, num_col) in locs:
        for (sym_row, sym_col) in symbol_locs:
            if abs(num_row - sym_row) <= 1 and abs(num_col - sym_col) <= 1:
                count_num[num_id] = True
                break

        if count_num[num_id] == True:
            break

print(sum([num for num, cond in zip(nums, count_num) if cond]))
