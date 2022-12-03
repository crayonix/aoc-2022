rucksacks = []

input_file = open("input.txt", "r")
lines = input_file.readlines()

for line in lines:
    line = line.replace("\n", "")
    midpoint = int(len(line) / 2)

    first_compartment = list(line[:midpoint])
    second_compartment = list(line[midpoint:])

    rucksacks.append([])

    rucksacks[-1].append(first_compartment)
    rucksacks[-1].append(second_compartment)


# part 1


def get_item_in_common(first_compartment, second_compartment):
    item = [value for value in first_compartment if value in second_compartment][0]
    return item


letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

total_priority = 0
for rucksack in rucksacks:
    first_compartment = rucksack[0]
    second_compartment = rucksack[1]

    in_common = get_item_in_common(first_compartment, second_compartment)
    total_priority += letters.index(in_common) + 1

print("Part 1: " + str(total_priority))
