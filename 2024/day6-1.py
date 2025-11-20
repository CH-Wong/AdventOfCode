import itertools
import sys
import os
import time

filename = "input_day6.txt"
with open(filename) as datafile:
    datamap = [[val for val in row] for row in datafile.read().split()]

print(datamap)

directions = {
    "^":(-1,0), 
    ">":(0,1), 
    "v":(1,0), 
    "<":(0,-1),
}

dir_cycle = itertools.cycle(directions)
print(dir_cycle)

cur_pos = None
cur_dir = None
for rownum, row in enumerate(datamap):
    for colnum, val in enumerate(row):
        # This allows for the puzzle to have arbitrary starting direction
        if val in ["^", ">", "v", "<"]:
            cur_pos = (rownum, colnum)
            cur_dir = val
            while next(dir_cycle) != val:
                pass

            break
    
    if cur_pos is not None:
        break


print(f"Starting position: {cur_pos}, starting direction {cur_dir}")

def vec_add(v1, v2):
    return tuple(x1 + x2 for x1, x2 in zip(v1, v2))


in_map = True
while in_map:
    datamap[cur_pos[0]][cur_pos[1]] = "X"
    next_pos = vec_add(cur_pos, directions[cur_dir])

    if 0 <= next_pos[0] < len(datamap) and 0 <= next_pos[1] < len(datamap[0]):
        if datamap[next_pos[0]][next_pos[1]] == "#":
            cur_dir = next(dir_cycle)
            cur_pos = vec_add(cur_pos, directions[cur_dir])
        else:
            cur_pos = next_pos
    else:
        in_map = False


    # map_print = "\n".join(["".join(row) for row in datamap]) 
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print(map_print)
    # time.sleep(1)

distinct_positions = 0
for rownum, row in enumerate(datamap):
    for colnum, val in enumerate(row):
        if val == "X":
            distinct_positions += 1

print(distinct_positions)
