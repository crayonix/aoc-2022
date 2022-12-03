rounds = []

input_file = open("input.txt", "r")
lines = input_file.readlines()

for line in lines:
    moves = line.split(" ")

    rounds.append([])

    rounds[-1].append(moves[0])
    rounds[-1].append(moves[1].replace("\n", ""))

# part 1

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


total_score_part_1 = 0
for _round in rounds:
    opponent_move = _round[0]
    my_move = _round[1]

    # always add your move to the total score
    total_score_part_1 += move_score[my_move]

    if opponent_did_tie(opponent_move, my_move):
        total_score_part_1 += 3
    elif not opponent_did_win(opponent_move, my_move):
        total_score_part_1 += 6


print("Part 1: " + str(total_score_part_1))

# part 2

move_score = {
    "rock": 1,  # rock
    "paper": 2,  # paper
    "scissors": 3,  # scissors
}


def get_tie_move_score(opponent_move):
    if opponent_move == OPPONENT_ROCK:
        return move_score["rock"]
    elif opponent_move == OPPONENT_PAPER:
        return move_score["paper"]
    elif opponent_move == OPPONENT_SCISSORS:
        return move_score["scissors"]


def get_winning_move_score(opponent_move):
    if opponent_move == OPPONENT_ROCK:
        return move_score["paper"]
    elif opponent_move == OPPONENT_PAPER:
        return move_score["scissors"]
    elif opponent_move == OPPONENT_SCISSORS:
        return move_score["rock"]


def get_losing_move_score(opponent_move):
    if opponent_move == OPPONENT_ROCK:
        return move_score["scissors"]
    elif opponent_move == OPPONENT_PAPER:
        return move_score["rock"]
    elif opponent_move == OPPONENT_SCISSORS:
        return move_score["paper"]


LOSE = "X"
TIE = "Y"
WIN = "Z"

outcome_score = {
    LOSE: 0,
    TIE: 3,
    WIN: 6,
}

total_score_part_2 = 0
for _round in rounds:
    opponent_move = _round[0]
    outcome = _round[1]

    total_score_part_2 += outcome_score[outcome]

    if outcome == TIE:
        total_score_part_2 += get_tie_move_score(opponent_move)
    elif outcome == WIN:
        total_score_part_2 += get_winning_move_score(opponent_move)
    elif outcome == LOSE:
        total_score_part_2 += get_losing_move_score(opponent_move)


print("Part 2: " + str(total_score_part_2))
