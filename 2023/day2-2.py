# Day 2-2
with open("input_day2.txt") as file:
    data = file.readlines()
colours = ["red", "green", "blue",]
max = [12, 13, 14]

max_dict = {c: m for c, m in zip(colours,max)}
print(max_dict)
game_id_sum = 0

for line in data:
    valid_game = True
    game_id, game_data = line.strip().split(": ")
    set_data = game_data.split("; ")
    for set in set_data:
        for hand in set.split(", "):
            amount, colour = hand.split(" ")
            print(amount, colour)
            if int(amount) > max_dict[colour]:
                valid_game = False

    if valid_game:

        game_id_sum += int(game_id.split(" ")[1])
     
print(game_id_sum)
