import numpy as np

with open("input_day9.txt") as datafile:
    head_movements = datafile.read().split("\n")

num_links = 9 + 1

movement_dict = {
    "R": np.array([1, 0]),
    "L": np.array([-1, 0]),
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
}

rope = [np.array([0,0]) for x in range(num_links)]
rope_movement_history = [rope]

for instruction in head_movements:
    direction, repetitions = instruction.split(" ")
    head_move = movement_dict[direction]

    for i in range(int(repetitions)):
        rope[0] += head_move

        for link_num in range(1, num_links):
            diff = rope[link_num-1] - rope[link_num]

            if np.linalg.norm(diff) > 2:
                rope[link_num] += np.array([int(diff[0]/abs(diff[0])), int(diff[1]/abs(diff[1]))])
                
            elif np.linalg.norm(diff) == 2:
                rope[link_num] += np.array([int(diff[0]/2), int(diff[1]/2)])

        rope_movement_history.append(np.copy(rope))

rope_movement_history = np.array(rope_movement_history)

print(len(set([tuple(pos) for pos in rope_movement_history[:,-1]])))