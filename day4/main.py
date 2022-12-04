elf_pairs = []

input_file = open("input.txt", "r")
lines = input_file.readlines()

for line in lines:
    line = line.strip()  # remove newline
    pair = line.split(",")

    elf_pairs.append([])
    elf_pairs[-1].append((int(pair[0].split("-")[0]),
                         int(pair[0].split("-")[1])))
    elf_pairs[-1].append((int(pair[1].split("-")[0]),
                         int(pair[1].split("-")[1])))

# part 1


def is_section_contained(section, subsection):
    for i in range(subsection[0], subsection[1] + 1):
        if not (section[0] <= i <= section[1]):
            return False
    return True


total_contained_sections = 0
for pair in elf_pairs:
    if is_section_contained(pair[0], pair[1]) or is_section_contained(pair[1], pair[0]):
        total_contained_sections += 1

print("Part 1: " + str(total_contained_sections))

# part 2


def is_section_overlapped(section, subsection):
    for i in range(subsection[0], subsection[1] + 1):
        if section[0] <= i <= section[1]:
            return True
    return False


total_overlapped_sections = 0
for pair in elf_pairs:
    if is_section_overlapped(pair[0], pair[1]) or is_section_overlapped(pair[1], pair[0]):
        total_overlapped_sections += 1

print("Part 2: " + str(total_overlapped_sections))
