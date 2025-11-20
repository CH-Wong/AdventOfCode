import re
import time

filename = "input_day9.txt"

with open(filename) as datafile:
    diskmap = datafile.read()

print(f"Diskmap imported, length: {len(diskmap)}")

disk = []
for id, (files, freespace) in enumerate(zip(diskmap[:-1:2], diskmap[1::2])):
    [disk.append(str(id)) for i in range(int(files))]
    [disk.append(".") for i in range(int(freespace))]

if len(diskmap) % 2 != 0:
    [disk.append(str(id+1)) for i in range(int(diskmap[-1]))]

# print(disk)

print(f"Diskmap decoded, length: {len(disk)}")

last_digit_index = len(disk) - 1
for pos, val in enumerate(disk):
    is_digit = False
    while not is_digit:
        if disk[last_digit_index] == ".":
            last_digit_index -= 1
        else:
            is_digit = True

    if val.isdigit():
        continue
    elif val == "." and pos <= last_digit_index:
        disk[pos] = disk[last_digit_index]
        disk[last_digit_index] = "."
    else:
        continue

# print(disk)

print("Diskmap Compressed")

checksum = 0
for n, id in enumerate(disk):
    if id.isdigit():
        checksum += n*int(id)
    else:
        continue

print(f"Checksum: {checksum}")


# print(diskmap)
# print(disk)

