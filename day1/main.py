import string


elves = [[]]

input_file = open("input.txt", "r")
lines = input_file.readlines()

for line in lines:
    if not line.isspace():
        elves[-1].append(int(line))
    else:
        elves.append([])

# part 1

max_calories = -1
for elf in elves:
    calories = sum(elf)
    if calories > max_calories:
        max_calories = calories

print(max_calories)

# part 2

calories_list = []
for elf in elves:
    calories = sum(elf)
    calories_list.append(calories)

calories_list.sort()
print(sum(calories_list[-3:]))
