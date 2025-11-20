filename = "input_day9.txt"
with open(filename) as datafile:
    diskmap = datafile.read()

files = [int(x) for x in diskmap[:-1:2]]
ids = [int(x) for x in range(len(files))]
freespace = [int(x) for x in diskmap[1::2]]

if len(diskmap) % 2 != 0:
    files.append(int(diskmap[-1]))
    ids.append(int(len(files)-1))

print(f"Diskmap imported, length: {len(diskmap)}")

index = len(files) - 1
while True:
    # print(ids, files, freespace)
    if index == 0:
        break

    for pos in range(len(freespace)):
        # These positions are not valid, as they are too the right of the file.
        if  pos >= index:
            break
        # Move file if it fits
        elif freespace[pos] >= files[index]:
            # 
            freespace[pos] -= files[index]
            freespace[index-1] += files[index]
            try:
                space = freespace.pop(index)
                freespace[index-1] += space
            except IndexError:
                pass
            
            freespace.insert(pos, 0)

            # Move filesize over to new position
            filesize = files.pop(index)
            files.insert(pos+1, filesize)

            # Move id over to new position
            id = ids.pop(index)
            ids.insert(pos+1, id)
        else:
            continue

    index -= 1

diskmap = ""
for file, space in zip(files, freespace):
    diskmap += str(file)
    diskmap += str(space)

if len(files) > len(freespace):
    diskmap += str(files[-1])

# print(diskmap)

disk = []
for id, file, space in zip(ids, files, freespace):
    [disk.append(str(id)) for i in range(int(file))]
    [disk.append(".") for i in range(int(space))]

if len(files) > len(freespace):
    [disk.append(str(ids[-1])) for i in range(int(diskmap[-1]))]

print(disk)

print(f"Diskmap decoded, length: {len(disk)}")

checksum = 0
for n, id in enumerate(disk):
    if id.isdigit():
        checksum += n*int(id)
    else:
        continue

print(f"Checksum: {checksum}")

# 7336349961969