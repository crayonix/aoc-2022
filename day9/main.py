import time
from os import system

moves = []

input_file = open("input.txt", "r")
lines = input_file.readlines()

for line in lines:
    line = line.strip()
    moves.append((line[0], int(line.split(" ")[-1])))

# Part 1

head = (0, 0)
tail = (0, 0)
visited_positions = {tail}


def get_knot_new_pos(front_knot, knot):
    x_diff = front_knot[0] - knot[0]
    y_diff = front_knot[1] - knot[1]

    if abs(x_diff) <= 1 and abs(y_diff) <= 1:
        return knot

    new_x = knot[0]
    new_y = knot[1]

    if abs(x_diff) > 1 and abs(y_diff) > 1:
        new_x = knot[0] + x_diff // 2
        new_y = knot[1] + y_diff // 2
    elif abs(x_diff) > 1 and abs(y_diff) >= 1:
        new_x = knot[0] + x_diff // 2
        new_y = knot[1] + y_diff
    elif abs(y_diff) > 1 and abs(x_diff) >= 1:
        new_y = knot[1] + y_diff // 2
        new_x = knot[0] + x_diff
    elif abs(x_diff) > 1:
        new_x = knot[0] + x_diff // 2
    elif abs(y_diff) > 1:
        new_y = knot[1] + y_diff // 2

    return (new_x, new_y)


for move in moves:
    for _ in range(move[1]):
        if move[0] == "U":
            head = (head[0] + 1, head[1])
        elif move[0] == "D":
            head = (head[0] - 1, head[1])
        elif move[0] == "R":
            head = (head[0], head[1] + 1)
        elif move[0] == "L":
            head = (head[0], head[1] - 1)

        tail = get_knot_new_pos(head, tail)

        visited_positions.add(tail)

print("Part 1: " + str(len(visited_positions)))

# Part 2

head = (0, 0)
knots = [(0, 0) for _ in range(1, 10)]


def print_grid():
    system('clear')
    for x in range(-10, 10):
        for y in range(-10, 10):
            to_print = "."
            if (-x, y) == (0, 0):
                to_print = "s"
            if (-x, y) in knots:
                to_print = str(knots.index((-x, y)) + 1)
            if (-x, y) == head:
                to_print = "H"
            print(to_print, end="")
        print()


visited_positions = {knots[-1]}
for move in moves:
    for _ in range(move[1]):
        if move[0] == "U":
            head = (head[0] + 1, head[1])
        elif move[0] == "D":
            head = (head[0] - 1, head[1])
        elif move[0] == "R":
            head = (head[0], head[1] + 1)
        elif move[0] == "L":
            head = (head[0], head[1] - 1)

        for i in range(len(knots)):
            # for debugging purposes
            # print_grid()
            # input("_")
            if i == 0:
                knots[i] = get_knot_new_pos(head, knots[i])
            else:
                knots[i] = get_knot_new_pos(knots[i - 1], knots[i])

        visited_positions.add(knots[-1])

print("Part 2: " + str(len(visited_positions)))
