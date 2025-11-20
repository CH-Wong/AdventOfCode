import numpy as np

with open("input_day9.txt") as datafile:
    head_movements = datafile.read().split("\n")

movement_dict = {
    "R": np.array([1, 0]),
    "L": np.array([-1, 0]),
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
}

head = np.array([0,0])
tail = np.array([0,0])
tail_movement_history = []

for instruction in head_movements:
    direction, repetitions = instruction.split(" ")
    head_move = movement_dict[direction]

    for i in range(int(repetitions)):
        head += head_move
        diff = head - tail

        if np.linalg.norm(diff) > 2:
            tail += np.array([int(diff[0]/abs(diff[0])), int(diff[1]/abs(diff[1]))])
            
        elif np.linalg.norm(diff) == 2:
            tail += head_move

        tail_movement_history.append(np.copy(tail))

print(len(set([tuple(pos) for pos in tail_movement_history])))