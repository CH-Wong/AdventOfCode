# Day 1-2
with open("input_day1.txt") as file:
    data = file.readlines()

str_replace = {
    "one": "o1ne", 
    "two": "t2wo", 
    "three": "t3hree", 
    "four": "f4our", 
    "five": "f5ive", 
    "six": "s6ix", 
    "seven": "s7even", 
    "eight": "e8ight", 
    "nine": "n9ine",
}

calibration = 0
for line in data:
    numbers = []
    for original, replacement in str_replace.items():
        line = line.replace(original, replacement)

    for character in line:
        if character.isnumeric():
            numbers.append(character)

    cal_val = numbers[0] + numbers[-1]
    print(cal_val)
    calibration += int(cal_val)

print(calibration)