with open("input_day4.txt") as file:
    data = file.readlines()

def get_score(num_winning_tickets):
    if num_winning_tickets == 0:
        return 0
    else:
        return 2**(num_winning_tickets - 1)

n_matching_numbers = []
for row in data:
    card_id, numbers = row.split(": ")
    card_id = card_id.split()[1]

    winning_nums, my_nums = numbers.split(" | ")

    winning_nums = [int(i) for i in winning_nums.split()]
    my_nums = [int(i) for i in my_nums.split()]

    winning_tickets = 0
    for n in my_nums:
        if n in winning_nums:
            winning_tickets += 1

    n_matching_numbers.append(winning_tickets)

tickets_won = [1 for i in range(len(data))]
for ind, n_win in enumerate(n_matching_numbers):
    for mult_ind in range(ind + 1, ind + n_win + 1):
        tickets_won[mult_ind] += tickets_won[ind]

print(tickets_won)
print(sum(tickets_won))
