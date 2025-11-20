import itertools
import sys
import os
import time
from copy import deepcopy

filename = "input_day6.txt"
with open(filename) as datafile:
    datamap = [[val for val in row] for row in datafile.read().split()]

directions = {
    "^":(-1,0), 
    ">":(0,1), 
    "v":(1,0), 
    "<":(0,-1),
}

dir_cycle = itertools.cycle(directions)
cur_pos = None
cur_dir = None
for rownum, row in enumerate(datamap):
    for colnum, val in enumerate(row):
        # This allows for the puzzle to have arbitrary starting direction
        if val in ["^", ">", "v", "<"]:
            cur_dir = val
            cur_pos = (rownum, colnum)
            break
    
    if cur_pos is not None:
        break

while next(dir_cycle) != cur_dir:
    pass

print(f"Starting position: {cur_pos}, starting direction {cur_dir}")

def vec_add(v1, v2):
    return tuple(x1 + x2 for x1, x2 in zip(v1, v2))

# This extra map is needed to track the extended vectors of the walk. For example during the first iteration, this entire extended vector should be saved.
# datamap:
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...

# extended_datamap:
# ....#.....
# ....^....#
# ....^.....
# ..#.^.....
# ....^..#..
# ....^.....
# .#..^.....
# ....^...#.
# #...^.....
# ....^.#...

def check_in_map(datamap, pos):
    return 0 <= pos[0] < len(datamap) and 0 <= pos[1] < len(datamap[0])



history = []
in_map = True
turn = True
sim = True

debug = False

n_blocks = 0
step_count = 0

block_locs = []

while in_map:
    # Print current situation
    step_count += 1
    print(f"Step: {step_count}")
    if debug:
        os.system('cls' if os.name == 'nt' else 'clear')
        map_print = "\n".join(["".join(row) for row in datamap]) 
        print(cur_dir, cur_pos)
        print(f"Map:\n{map_print}\n")
        time.sleep(0.1)

    # Reset the directions
    while next(dir_cycle) != cur_dir:
        pass

    # This writes an arrow in the map at the current position. During this iteration we will move a to a new position.
    datamap[cur_pos[0]][cur_pos[1]] = cur_dir

    ## Check next position
    next_pos = vec_add(cur_pos, directions[cur_dir])
    # If next position is outside of map, then the loop should end by setting in_map to false.
    if not check_in_map(datamap, next_pos):
        in_map = False

    # If we are in the map, let's check for blockades marked by #. 
    # Here turning logic must be added.
    # We turn in place for one turn to allow for a check if the block on the right.
    # Immediately making a right turn would effectively skip the check on our block on the right.
    elif datamap[next_pos[0]][next_pos[1]] == "#":
        next_dir = next(dir_cycle)
        next_pos = cur_pos

    # If no blockade is found, we set the next_dir to be the same as before.
    else:
        next_dir = cur_dir
        turn = False
    

        # Everytime we took a turn, we will run a simulation run to continue it with a block placed in front of the guard.
        # The second statement checks if there was a turn in place. This would result in double counting if not added.
        if sim and cur_pos not in [entry[0] for entry in history]:
            sim_stuck = False
            sim_in_map = True

            sim_history = deepcopy(history)
            sim_cur_pos = deepcopy(cur_pos)
            sim_cur_dir = deepcopy(cur_dir)
            sim_next_pos = deepcopy(next_pos)
            sim_next_dir = deepcopy(next_dir)
            sim_map = deepcopy(datamap)
            sim_map[next_pos[0]][next_pos[1]] = "#"

            while sim_in_map and not sim_stuck:
                # Print current situation
                if debug:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    map_print = "\n".join(["".join(row) for row in sim_map]) 
                    print(sim_cur_dir, sim_cur_pos)
                    print(f"Simulated Map for {cur_pos}:\n{map_print}\nSuccesses: {n_blocks}")
                    time.sleep(0.01)

                # Reset the directions
                while next(dir_cycle) != sim_cur_dir:
                    pass

                # This writes an arrow in the map at the current position. During this iteration we will move a to a new position.
                sim_map[sim_cur_pos[0]][sim_cur_pos[1]] = sim_cur_dir

                ## Check next position
                sim_next_pos = vec_add(sim_cur_pos, directions[sim_cur_dir])
                # If next position is outside of map, then the loop should end by setting in_map to false.
                if not check_in_map(sim_map, sim_next_pos):
                    sim_in_map = False

                # If we are in the map, let's check for blockades marked by #. 
                # Here turning logic must be added.
                # We turn in place for one turn to allow for a check if the block on the right.
                # Immediately making a right turn would effectively skip the check on our block on the right.
                elif sim_map[sim_next_pos[0]][sim_next_pos[1]] == "#":
                    sim_next_dir = next(dir_cycle)
                    sim_next_pos = sim_cur_pos

                # If no blockade is found, we set the next_dir to be the same as before.
                else:
                    sim_next_dir = sim_cur_dir

                # If we have been in this position with the same direction, that means we are starting a loop.
                # Break out of the while loop by setting stuck = True
                if (sim_cur_pos, sim_cur_dir) in sim_history:
                    sim_stuck = True
                    n_blocks += 1
                    block_locs.append(next_pos)
                    # print('STUCK')
                    # input()
                else:
                    sim_history.append((sim_cur_pos, sim_cur_dir))

                # Update our position and direction
                sim_cur_dir = sim_next_dir
                sim_cur_pos = sim_next_pos


    # If we have been in this position with the same direction, that means we are starting a loop.
    # Break out of the while loop by setting stuck = True
    if (cur_pos, cur_dir) in history:
        history.append((cur_pos, cur_dir))

    # Update our position and direction
    cur_dir = next_dir
    cur_pos = next_pos

print(len(set(block_locs)))

print(n_blocks)