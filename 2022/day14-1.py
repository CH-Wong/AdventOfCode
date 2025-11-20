import matplotlib.pyplot as plt
import numpy as np

with open("input_day14.txt") as datafile:
    scan_data = datafile.read().strip().split("\n")

corners = []
for rock_line in scan_data:
    line = rock_line.split(" -> ")
    for corner in line:
        x, y = corner.split(",")
        corners.append((int(x), int(y)))

corners = np.array(corners)
xlim = ((np.min(corners[:,0]) - 10), (np.max(corners[:,0] + 10)))
ylim = ((np.min(corners[:,1]) - 10), (np.max(corners[:,1]) + 10))


source = (500,0)

field = np.zeros((xlim[1], ylim[1] + 1))

for rock_line in scan_data:
    corners = rock_line.split(" -> ")
    for pos1, pos2 in zip(corners[:-1], corners[1:]):
        x1, y1 = [int(val) for val in pos1.split(",")]
        x2, y2 = [int(val) for val in pos2.split(",")]

        if x1 == x2:
            field[x1, min([y1, y2]):max([y1, y2]) + 1].fill(True)

        elif y1 == y2:
            field[min([x1, x2]): max([x1, x2]) + 1, y1].fill(True)

fig = plt.figure()
plt.imshow(field.transpose(), interpolation='nearest')
plt.xlim(xlim)
plt.ylim(ylim)
plt.xlabel("x")
plt.ylabel("y")
plt.gca().invert_yaxis()

current_pos = source
abyss = False
sand_added = 0 
while abyss == False:
    # print(current_pos)
    if current_pos[1] == ylim[1]:
        abyss = True

    elif not field[current_pos[0], current_pos[1] + 1]:
        current_pos = (current_pos[0], current_pos[1] + 1)

    elif not field[current_pos[0] - 1, current_pos[1] + 1]:
        current_pos = (current_pos[0] - 1, current_pos[1] + 1)

    elif not field[current_pos[0] + 1, current_pos[1] + 1]:
        current_pos = (current_pos[0] + 1, current_pos[1] + 1)

    else:

        field[current_pos[0], current_pos[1]] = True
        current_pos = source
        sand_added += 1

print(sand_added)



fig = plt.figure()

plt.imshow(field.transpose(), interpolation='nearest')
plt.xlim(xlim)
plt.ylim(ylim)
plt.xlabel("x")
plt.ylabel("y")
plt.gca().invert_yaxis()
plt.show()