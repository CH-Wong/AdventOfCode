import math

filename = "input_day11.txt"
with open(filename) as datafile:
    stones = [int(val) for val in datafile.read().split()]

print(stones)


def n_digits(num):
    return int(math.log10(num) + 1)


def first_n_digits(num, n):
    return int(num // 10 ** (int(math.log(num, 10)) - n + 1))

def last_n_digits(num, n):
    first_digits = first_n_digits(num, n_digits(num) - n)
    return int(num - first_digits * 10 ** n)

for i in range(75):
    print(i, len(stones))
    new_stones = []
    for pos, val in enumerate(stones):
        to_be_inserted = []
        if val == 0:
            new_stones.append(1)
        
        elif n_digits(val) % 2 == 0:
            new_stones.append(first_n_digits(val,n_digits(val)/2))
            new_stones.append(last_n_digits(val,n_digits(val)/2))

        else:
            new_stones.append(val*2024)
    
        # print(pos,val,new_stones)

    stones = [stone for stone in new_stones]

    # print(stones)

print(len(stones))
