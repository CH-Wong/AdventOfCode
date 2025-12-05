def decode_diskmap(diskmap, register=None):    
    filesizes = [int(bit) for bit in diskmap[::2]]
    freesizes = [int(bit) for bit in diskmap[1::2]]

    print(filesizes)
    print(freesizes)

    disk = []
    if register == None:
        for filenum, (filesize, freesize) in enumerate(zip(filesizes, freesizes)):
            print(filenum)
            for _ in range(filesize):
                disk.append(filenum)
            for _ in range(freesize):
                disk.append(0)

        if len(diskmap) % 2 != 0:
            for _ in range(filesizes[-1]):
                disk.append(filenum+1)

    else:
        for filenum, filesize, freesize in zip(register, filesizes, freesizes):
            for _ in range(filesize):
                disk.append(filenum)
            for _ in range(freesize):
                disk.append(0)    
    
        if len(diskmap) % 2 != 0:
            for _ in range(filesizes[-1]):
                disk.append(register[-1])

    return disk

def get_checksum(disk):
    checksum = 0
    for n, id in enumerate(disk):
        checksum += n*int(id)
    print(f"Checksum: {checksum}")
    return checksum

filename = "input_day9.txt"
folder = "./2024/"
with open(folder + filename) as datafile:
    diskmap = datafile.read()

filesizes = [int(bit) for bit in diskmap[0::2]]
freespaces = [int(bit) for bit in diskmap[1::2]]

disk = decode_diskmap(diskmap, range(len(filesizes)))
file_id_register = [index for index in range(len(filesizes))]

current_file_id = file_id_register[-1]

while current_file_id >= 0:
    print(current_file_id)
    current_file_index = file_id_register.index(current_file_id)

    current_file_size = filesizes[current_file_index]
    file_id = file_id_register[current_file_index]

    for index_space, space in enumerate(freespaces):
        if index_space == current_file_index:
            print("HANDLED FILES")
            break

        if current_file_size <= space:
            print("FOUND SPOT", space, current_file_size)
            del filesizes[current_file_index]
            try:
                current_space = freespaces.pop(current_file_index)
                freespaces[current_file_index-1] += current_file_size + current_space
            except IndexError:
                pass

            new_space = space - current_file_size
            freespaces[index_space] = 0

            freespaces.insert(index_space+1, new_space)
            filesizes.insert(index_space+1, current_file_size)

            del file_id_register[-1]
            file_id_register.insert(file_id, index_space + 1)

            break
        else:
            continue

    current_file_id -= 1

diskmap = []
for size, space in zip(filesizes, freespaces):
    diskmap.append(size)
    diskmap.append(space) 

if len(diskmap) % 2 != 0:
    diskmap.append(filesizes[-1])

print("AFTER DEFRAGGING -----------------------")
print(f"# of files: {len(file_id_register)}")
disk = decode_diskmap(diskmap,file_id_register)
print(f"disk size: {len(disk)}")
print(disk)
print(file_id_register)

checksum = get_checksum(disk)
print(checksum)