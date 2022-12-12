
input_file = open("input.txt", "r")
lines = input_file.readlines()

instructions = []

for line in lines:
    line = line.strip()
    instruction = line.split(" ")[0]
    param = None if "noop" == instruction else int(line.split(" ")[-1])
    cycles = 1 if "noop" == instruction else 2

    instructions.append((instruction, param, cycles))

# Part 1

register_x = 1
current_cycle = 1
signal_strengths = []
cycle_milestones = [20, 60, 100, 140, 180, 220]

for instruction in instructions:
    for i in range(instruction[2]):
        if instruction[0] == "noop":
            current_cycle += 1

        elif instruction[0] == "addx":
            current_cycle += 1
            if i == instruction[2] - 1:
                register_x += instruction[1]

        if current_cycle in cycle_milestones:
            signal_strengths.append(register_x * current_cycle)

        # print("Cycle " + str(current_cycle) + ": " + str(register_x))

print("Part 1: " + str(sum(signal_strengths)))
