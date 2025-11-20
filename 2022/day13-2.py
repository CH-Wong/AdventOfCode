with open("input_day13.txt") as datafile:
    packets = datafile.read().strip().split("\n")

packets = [eval(packet) for packet in packets if packet != ""]
packets.append([[2]])
packets.append([[6]])

def check_packet(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        elif left > right:
            return False
        elif left == right:
            return None
        else:
            print("???!?!?!?!")

    elif type(left) == int and type(right) == list:
        return check_packet([left], right)

    elif type(left) == list and type(right) == int:
        return check_packet(left, [right])

    elif type(left) == list and type(right) == list:
        for index in range(max([len(left), len(right)])):
            if index == len(left) and index != len(right):
                return True
                
            elif index != len(left) and index == len(right):
                return False

            else:
                l = left[index]
                r = right[index]
                packet_result = check_packet(l, r)

                if packet_result == None:
                    continue
                else:
                    return packet_result
                
    else:
        print("?!?!?!?!")

iteration = 0
sorted_succesful = False

while sorted_succesful == False:
    iteration += 1

    sorting_status = []

    for index in range(len(packets)-1):
        left = packets[index]
        right = packets[index + 1]

        if check_packet(left, right):
            sorting_status.append(True)
        else:
            packets[index] = right
            packets[index + 1] = left
            sorting_status.append(False)

    if all(sorting_status):
        sorted_succesful = True
        
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
