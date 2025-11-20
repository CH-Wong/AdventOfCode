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

antinode_locs = []

count = 0
for antenna_type, locations in antenna_locs.items():
    for antenna1, antenna2 in itertools.combinations(locations, 2):
        print(antenna_type, antenna1, antenna2)
        
        # Add both directions to the antinodes:
        antinode1 = antenna1 + 2*(antenna2 - antenna1)
        if xlim[0] <= antinode1.real <= xlim[1] and ylim[0] <= antinode1.imag <= ylim[1]:
            antinode_locs.append(antinode1)


        antinode2 = antenna2 + 2*(antenna1 - antenna2)
        if xlim[0] <= antinode2.real <= xlim[1] and ylim[0] <= antinode2.imag <= ylim[1]:
            antinode_locs.append(antinode2)



    # # extract real part 
    # x = [ele.real for ele in locations] 
    # # extract imaginary part 
    # y = [ele.imag for ele in locations]

    # plt.scatter(x, y)


print(len(set(antinode_locs)))
print(count)

# for node in antinode_locs:
#     plt.scatter(node.real, node.imag, c="r", marker="x")

# plt.gca().invert_xaxis()
# plt.gca().invert_yaxis()
# plt.show()
