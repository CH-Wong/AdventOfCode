def your_score(opponent, you):
    rps_dict = {
        "X": 1,
        "Y": 2,
        "Z": 3,
        "A": 1,
        "B": 2,
        "C": 3,
    }
    

    opponent_value = rps_dict[opponent]
    your_value = rps_dict[you]

    result = your_value - opponent_value 
    # Draw
    if result == 0:
        return your_value + 3
    elif result == 1 or result == -2:
        return your_value + 6
    else:
        return your_value


with open("input_day2.txt") as datafile:
    tournament_data = datafile.read()

total_score = 0

for game in tournament_data.split("\n"):
    opponent, you = game.split(" ")
    total_score += your_score(opponent, you)

print(total_score)