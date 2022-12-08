from collections import deque
import copy

stacks = []
moves = []

input_file = open("input.txt", "r")
lines = input_file.readlines()

for line in lines:
    if line.isspace():
        continue
    elif "move" in line:
        # remove all except numbers
        line = line.replace("move ", "")
        line = line.replace(" from ", ",")
        line = line.replace(" to ", ",")
        moves.append(line.strip().split(","))
    elif "1" in line:
        continue
    else:
        # group line into 4 character chunks
        containers = [line[x:x+4] for x in range(0, len(line), 4)]

        # add containers to matrix
        for i in range(len(containers)):
            container = containers[i][1]

            if i >= len(stacks):
                stacks.append(deque())

            if container.isspace():
                continue

            stacks[i].appendleft(container)

# part 1

stacks_one = copy.deepcopy(stacks)
for move in moves:
    containers = int(move[0])
    from_stack = int(move[1])-1
    to_stack = int(move[2])-1

    for i in range(containers):
        stacks_one[to_stack].append(stacks_one[from_stack].pop())


top_crates = ""
for stack in stacks_one:
    top_crates += stack[-1]

print("Part 1: " + top_crates)

# part 2

stacks_two = copy.deepcopy(stacks)
for move in moves:
    containers = int(move[0])
    from_stack = int(move[1])-1
    to_stack = int(move[2])-1

    stack = list(stacks_two[from_stack])
    stacks_two[to_stack].extend(stack[-containers:])
    stacks_two[from_stack] = deque(stack[:-containers])

top_crates = ""
for stack in stacks_two:
    top_crates += stack[-1]

print("Part 2: " + top_crates)
