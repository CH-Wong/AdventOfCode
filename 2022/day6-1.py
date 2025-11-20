with open("input_day6.txt") as datafile:
    datastream = datafile.read()

for index in range(len(datastream)-3):
    if len(set(datastream[index:index+4])) == 4:
        print(index + 4)
        break