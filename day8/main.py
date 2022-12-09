matrix = []

input_file = open("input.txt", "r")
lines = input_file.readlines()

for line in lines:
    matrix.append([int(num) for num in list(line.strip())])

# part 1

visible_tree_count = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix[i])-1:
            visible_tree_count += 1
            continue

        tree_size = matrix[i][j]

        left_visible = True
        for left_tree_size in matrix[i][:j]:
            if left_tree_size >= tree_size:
                left_visible = False
                break

        right_visible = True
        for right_tree_size in matrix[i][j+1:]:
            if right_tree_size >= tree_size:
                right_visible = False
                break

        up_visible = True
        for up_rows in matrix[:i]:
            up_tree_size = up_rows[j]
            if up_tree_size >= tree_size:
                up_visible = False
                break

        down_visible = True
        for down_rows in matrix[i+1:]:
            down_tree_size = down_rows[j]
            if down_tree_size >= tree_size:
                down_visible = False
                break

        if left_visible or right_visible or up_visible or down_visible:
            visible_tree_count += 1

print("Part 1: " + str(visible_tree_count))

# part 2

max_scenic_score = -1

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        tree_size = matrix[i][j]

        left_tree_count = 0
        if i != 0:
            left_column = matrix[i][:j]
            left_column.reverse()
            for left_tree_size in left_column:
                left_tree_count += 1
                if left_tree_size >= tree_size:
                    break

        right_tree_count = 0
        if i != len(matrix)-1:
            right_column = matrix[i][j+1:]
            for right_tree_size in right_column:
                right_tree_count += 1
                if right_tree_size >= tree_size:
                    break

        up_tree_count = 0
        if j != 0:
            up_rows = matrix[:i]
            up_rows.reverse()
            for up_row in up_rows:
                up_tree_count += 1
                up_tree_size = up_row[j]
                if up_tree_size >= tree_size:
                    break

        down_tree_count = 0
        if j != len(matrix[i])-1:
            down_rows = matrix[i+1:]
            for down_row in down_rows:
                down_tree_count += 1
                down_tree_size = down_row[j]
                if down_tree_size >= tree_size:
                    break

        scenic_score = left_tree_count * right_tree_count * up_tree_count * down_tree_count
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print("Part 2: " + str(max_scenic_score))
