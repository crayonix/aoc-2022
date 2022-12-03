from functools import reduce
import numpy

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


def get_items_in_common(items_one, items_two):
    items = [value for value in items_one if value in items_two]
    return items


letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

total_priority_part_one = 0
for rucksack in rucksacks:
    first_compartment = rucksack[0]
    second_compartment = rucksack[1]

    in_common = get_items_in_common(first_compartment, second_compartment)[0]
    total_priority_part_one += letters.index(in_common) + 1

print("Part 1: " + str(total_priority_part_one))

# part 2

rucksack_groups = [[y[0]+y[1] for y in rucksacks][x:x+3]
                   for x in range(0, len(rucksacks), 3)]

total_priority_part_two = 0
for rucksack_group in rucksack_groups:
    rucksack_one = rucksack_group[0]
    rucksack_two = rucksack_group[1]
    rucksack_three = rucksack_group[2]

    in_common = reduce(numpy.intersect1d,
                       (rucksack_one, rucksack_two, rucksack_three))[0]
    total_priority_part_two += letters.index(in_common) + 1

print("Part 2: " + str(total_priority_part_two))
