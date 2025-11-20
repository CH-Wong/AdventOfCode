filename = "input_day4.txt"
with open(filename) as datafile:
    data = [[val for val in row] for row in datafile.readlines()]

def vec_add(v1, v2):
    return tuple(x1 + x2 for x1, x2 in zip(v1, v2))

def vec_sub(v1, v2):
    return tuple(x1 - x2 for x1, x2 in zip(v1, v2))

def look_around(data, pos, target, allowed_dir="all"):
    directions = [
        (1,0),
        (1,1),
        (0,1),
        (-1,1),
        (-1,0),
        (-1,-1),
        (0,-1),
        (1,-1),
    ]

    matching_locs = []
    for dir in directions:
        next_loc = vec_add(pos, dir)
        if 0 <= next_loc[0] < len(data) and 0 <= next_loc[1] < len(data[0]) and data[next_loc[0]][next_loc[1]] == target and (dir == allowed_dir or allowed_dir == "all"):
            matching_locs.append(next_loc)

    return matching_locs 

all_Xs = []
for rownum, row in enumerate(data):
    for colnum, val in enumerate(row):
        if val == "X":
            all_Xs.append((rownum, colnum))

XMAS_count = 0

for x in all_Xs:
    all_Ms = look_around(data, x, "M")
    for m in all_Ms:
        all_As = look_around(data, m, "A", vec_sub(m, x))
        for a in all_As:
            all_Ss = look_around(data, a, "S", vec_sub(a, m))
            for s in all_Ss:
                # print(x, m, a, s)
                XMAS_count += 1

print(XMAS_count)