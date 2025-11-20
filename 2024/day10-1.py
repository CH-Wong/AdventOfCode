from copy import deepcopy

filename = "input_day10.txt"
with open(filename) as datafile:
    datamap = [[int(val) for val in row] for row in datafile.read().split()]

for row in datamap:
    print(row)

trailheads = []
peaks = []
for rownum, row in enumerate(datamap):
    for colnum, height in enumerate(row):
        if height == 0:
            trailheads.append((rownum, colnum))
        elif height == 9:
            peaks.append((rownum, colnum))

print("TRAILHEADS:")
for pos in trailheads:
    print(pos)

print("PEAKS:")
for pos in peaks:
    print(pos)

directions = [
    (-1,0), 
    (0,1), 
    (1,0), 
    (0,-1),
]

def vec_add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def in_map(pos):
    return 0 <= pos[0] < len(datamap[0]) and 0 <= pos[1] < len(datamap)

def search_nb(source):
    height = datamap[source[0]][source[1]]
    valid_neighbours = []
    for d in directions:
        nb = vec_add(source, d)
        if in_map(nb) and datamap[nb[0]][nb[1]] == height + 1:
            valid_neighbours.append(nb)
    return valid_neighbours
    
print("\n\n")
score = 0
for starting_pos in trailheads:
    searching = [starting_pos]
    peaks_reached = []

    while len(searching) > 0:
        to_search = []
        # print(searching)
        for pos in searching:
            nbs = search_nb(pos)
            # print(nbs)
            for nb in nbs:
                if datamap[nb[0]][nb[1]] == 9 and nb not in peaks_reached:
                    print(f"Peak: {nb}")
                    peaks_reached.append(nb)
                else:
                    to_search.append(nb)
        
        searching = deepcopy(to_search)

    # print(starting_pos, len(peaks_reached))
    score += len(peaks_reached)

print(score)