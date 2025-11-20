with open("input_day6.txt") as datafile:
    datastream = datafile.read()

marker_length = 14

for index in range(len(datastream)-marker_length):
    if len(set(datastream[index:index+marker_length])) == marker_length:
        print(index + marker_length)
        break