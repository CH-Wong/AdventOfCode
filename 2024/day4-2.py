filename = "input_day4.txt"
with open(filename) as datafile:
    data = [[val for val in row] for row in datafile.readlines()]

def vec_add(v1, v2):
    return tuple(x1 + x2 for x1, x2 in zip(v1, v2))

def vec_sub(v1, v2):
    return tuple(x1 - x2 for x1, x2 in zip(v1, v2))

def look_around(data, pos):
    directions = [
        (1,1),
        (-1,1),
        (-1,-1),
        (1,-1),
    ]

    matching_locs = []
    for dir in directions:
        next_loc = vec_add(pos, dir)
        if 0 <= next_loc[0] < len(data) and 0 <= next_loc[1] < len(data[0]):
            matching_locs.append(next_loc)

    return matching_locs 

all_As = []
for rownum, row in enumerate(data):
    for colnum, val in enumerate(row):
        if val == "A":
            all_As.append((rownum, colnum))

X_MAS_count = 0

valid_results = [
    "MMSS",
    "SMMS", 
    "SSMM", 
    "MSSM",
]

for a in all_As:
    matching_locs = look_around(data, a)
    if len(matching_locs) == 4:
        values = "".join([data[loc[0]][loc[1]] for loc in matching_locs])
        if values in valid_results:
            X_MAS_count += 1

print(X_MAS_count)