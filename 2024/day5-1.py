import math

filename = "input_day5.txt"
with open(filename) as datafile:
    data = datafile.read()

rules, updates = data.split("\n\n")

rules = [r.split("|") for r in rules.split()]
updates = [u.split(",") for u in updates.split()]

middle_numbers = []
for u in updates:
    update_correct = True

    for cur_ind, cur_num in enumerate(u):
        other_numbers = u.copy()
        del other_numbers[cur_ind]

        for r in rules:
            if r[0] == cur_num and r[1] in other_numbers:
                oth_ind = u.index(r[1])
                oth_num = r[1]

                if cur_ind > oth_ind:
                    update_correct = False
                    break

            if not update_correct:
                break
        
        if not update_correct:
            break

    if update_correct:
        middle_number = int(u[math.floor(len(u)/2)])
        middle_numbers.append(middle_number)

print(sum(middle_numbers)) 