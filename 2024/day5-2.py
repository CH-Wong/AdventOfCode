import math

filename = "input_day5.txt"
with open(filename) as datafile:
    data = datafile.read()

rules, updates = data.split("\n\n")

rules = [r.split("|") for r in rules.split()]
updates = [u.split(",") for u in updates.split()]

incorrect_updates = []
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

    if not update_correct:
        incorrect_updates.append(u)

corrected_updates = []
for u in incorrect_updates:
    update_correct = False

    while not update_correct:
        update_correct = True
        for cur_ind, cur_num in enumerate(u):
            other_numbers = u.copy()
            del other_numbers[cur_ind]

            for r in rules:
                if r[0] == cur_num and r[1] in other_numbers:
                    oth_ind = u.index(r[1])
                    oth_num = r[1]
                    
                    if cur_ind > oth_ind:
                        del u[cur_ind]    
                        u.insert(oth_ind, cur_num)
                        update_correct = False

                        break

                if not update_correct:
                    break
            
            if not update_correct:
                break
    corrected_updates.append(u)

middle_numbers = []
for u in corrected_updates:
    middle_number = int(u[math.floor(len(u)/2)])
    middle_numbers.append(middle_number)

print(sum(middle_numbers)) 