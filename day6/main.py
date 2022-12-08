
input_file = open("input.txt", "r")
buffer = input_file.readlines()[0]

# part 1
first_marker_position = -1
for i in range(len(buffer)):
    subbuffer = ""
    marker_count = 0
    for j in range(i, len(buffer)):
        if marker_count == 4:
            first_marker_position = j
            break
        elif buffer[j] in subbuffer:
            break
        else:
            subbuffer += buffer[j]
            marker_count += 1

    if first_marker_position != -1:
        break

print("Part 1: " + str(first_marker_position))

# part 2
second_marker_position = -1
for i in range(len(buffer)):
    subbuffer = ""
    marker_count = 0
    for j in range(i, len(buffer)):
        if marker_count == 14:
            second_marker_position = j
            break
        elif buffer[j] in subbuffer:
            break
        else:
            subbuffer += buffer[j]
            marker_count += 1

    if second_marker_position != -1:
        break

print("Part 2: " + str(second_marker_position))
