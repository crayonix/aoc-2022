rounds = []

input_file = open("input.txt", "r")
lines = input_file.readlines()

for line in lines:
    moves = line.split(" ")

    rounds.append([])

    rounds[-1].append(moves[0])
    rounds[-1].append(moves[1].replace("\n", ""))


move_score = {
    "X": 1,  # rock
    "Y": 2,  # paper
    "Z": 3,  # scissors
}

OPPONENT_ROCK = "A"
OPPONENT_PAPER = "B"
OPPONENT_SCISSORS = "C"
MY_ROCK = "X"
MY_PAPER = "Y"
MY_SCISSORS = "Z"


def opponent_did_win(opponent_move, my_move):
    if opponent_move == OPPONENT_ROCK:
        return my_move == MY_SCISSORS
    elif opponent_move == OPPONENT_PAPER:
        return my_move == MY_ROCK
    elif opponent_move == OPPONENT_SCISSORS:
        return my_move == MY_PAPER


def opponent_did_tie(opponent_move, my_move):
    if opponent_move == OPPONENT_ROCK:
        return my_move == MY_ROCK
    elif opponent_move == OPPONENT_PAPER:
        return my_move == MY_PAPER
    elif opponent_move == OPPONENT_SCISSORS:
        return my_move == MY_SCISSORS


total_score = 0
for _round in rounds:
    opponent_move = _round[0]
    my_move = _round[1]

    # always add your move to the total score
    total_score += move_score[my_move]

    if opponent_did_tie(opponent_move, my_move):
        total_score += 3
    elif not opponent_did_win(opponent_move, my_move):
        total_score += 6

print(total_score)
