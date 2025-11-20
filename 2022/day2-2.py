def your_score(opponent, result):
    rps_dict = {
        "X": 0,
        "Y": 3,
        "Z": 6,
        "A": 1,
        "B": 2,
        "C": 3,
    }
    
    result = rps_dict[result]
    opponent_value = rps_dict[opponent]

    # Draw
    if result == 3:
        return result + opponent_value

    # Lose
    elif result == 0:
        if opponent_value - 1 == 0:
            return result + 3
        else:
            return  result + opponent_value - 1

    # Win
    elif result == 6:
        if opponent_value + 1 == 4:
            return result + 1
        else:
            return  result + opponent_value + 1



with open("input_day2.txt") as datafile:
    tournament_data = datafile.read()

total_score = 0

for game in tournament_data.split("\n"):
    opponent, you = game.split(" ")
    total_score += your_score(opponent, you)

print(total_score)