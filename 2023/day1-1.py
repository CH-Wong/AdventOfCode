# Day 1-1
with open("input_day1.txt") as file:
    data = file.readlines()

calibration = 0
for line in data:
    numbers = []
    for character in line:
        if character.isnumeric():
            numbers.append(character)

    cal_val = numbers[0] + numbers[-1]
    print(cal_val)
    calibration += int(cal_val)

print(calibration)