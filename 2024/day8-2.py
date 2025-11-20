import matplotlib.pyplot as plt
import itertools

filename = "input_day8.txt"

antenna_locs = {}
with open(filename) as datafile:
    for y, row in enumerate(datafile.read().split()):
        for x, val in enumerate(row):
            if val != ".":
                try:
                    antenna_locs[val].append(complex(x,y))

                except KeyError:
                    antenna_locs[val] = [complex(x,y)]

xlim = (0, x)
ylim = (0, y)

def in_map(node, xlim, ylim):
    return xlim[0] <= node.real <= xlim[1] and ylim[0] <= node.imag <= ylim[1]

antinode_locs = []
for antenna_type, locations in antenna_locs.items():
    for antenna1, antenna2 in itertools.combinations(locations, 2):
        print(antenna_type, antenna1, antenna2)

        pos_vec = antenna2 - antenna1
        neg_vec = antenna1 - antenna2

        # Handle positives first
        multiplier = 0
        while True:
            antinode = antenna2 + multiplier*pos_vec
            if in_map(antinode, xlim, ylim):
                antinode_locs.append(antinode)
                multiplier += 1
            else:
                break

        multiplier = 0
        while True:
            antinode = antenna1 + multiplier*neg_vec
            if in_map(antinode, xlim, ylim):
                antinode_locs.append(antinode)
                multiplier += 1
            else:
                break

    # # extract real part 
    # x = [ele.real for ele in locations] 
    # # extract imaginary part 
    # y = [ele.imag for ele in locations]

    # plt.scatter(x, y)


print(len(set(antinode_locs)))

# for node in antinode_locs:
#     plt.scatter(node.real, node.imag, c="r", marker="x")

# plt.gca().invert_xaxis()
# plt.gca().invert_yaxis()
# plt.show()
