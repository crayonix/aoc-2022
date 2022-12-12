import time

moves = []

input_file = open("input.txt", "r")
lines = input_file.readlines()

for line in lines:
    line = line.strip()
    moves.append((line[0], int(line.split(" ")[-1])))

head = (0, 0)
tail = (0, 0)
visited_positions = {tail}


def get_tails_new_pos(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]

    if abs(x_diff) <= 1 and abs(y_diff) <= 1:
        return tail

    new_x = tail[0]
    new_y = tail[1]

    if abs(x_diff) > 1 and abs(y_diff) >= 1:
        new_x = tail[0] + x_diff // 2
        new_y = tail[1] + y_diff
    elif abs(y_diff) > 1 and abs(x_diff) >= 1:
        new_y = tail[1] + y_diff // 2
        new_x = tail[0] + x_diff
    elif abs(x_diff) > 1:
        new_x = tail[0] + x_diff // 2
    elif abs(y_diff) > 1:
        new_y = tail[1] + y_diff // 2

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

        tail = get_tails_new_pos(head, tail)

        visited_positions.add(tail)

print("Part 1: " + str(len(visited_positions)))
