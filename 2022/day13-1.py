with open("input_day13.txt") as datafile:
    packets = datafile.read().strip().split("\n\n")

def check_packet(left, right):
    print(left)
    print(right)
    # input()
    if type(left) == int and type(right) == int:
        if left < right:
            print("Left value smaller.")
            return True
        elif left > right:
            print("Right value smaller.")
            return False
        elif left == right:
            print("Same value.")
            return None
        else:
            print("???!?!?!?!")


    elif type(left) == int and type(right) == list:
        print("converting to list")
        return check_packet([left], right)

    elif type(left) == list and type(right) == int:
        print("converting to list")
        return check_packet(left, [right])

    elif type(left) == list and type(right) == list:
        print("comparing lists")
        for index in range(max([len(left), len(right)])):
            if index == len(left) and index != len(right):
                print("Left side smaller, passesd.")
                return True
                
            elif index != len(left) and index == len(right):
                print("Right side smaller, passesd.")
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
    
correctly_ordered = []

for packet_num, packet in enumerate(packets):
    left, right = packet.split("\n")

    left = eval(left)
    right = eval(right)

    print(f"Packet #: {packet_num + 1} ---------------------")
    if check_packet(left, right):
        print("Packet Passed.")
        correctly_ordered.append(packet_num + 1)
    else:
        print("Packet Failed.")

print(sum(correctly_ordered))