from typing import Dict, Tuple, List


def parse_input() -> List[List[List]]:
    patterns = []
    with open("input.txt") as f:
        pattern = []
        count = 0
        for line in f:
            line_pattern = []
            if line == "\n":
                print(pattern)
                count += 1
                patterns.append(pattern)
                pattern = []
                continue
            for char in line:
                print(char)
                if char == "\n":
                    pattern.append(line_pattern)
                    break
                line_pattern.append(char)
    return patterns


patterns = parse_input()
# print(patterns[-1])


def is_horizontal_reflection(index, pattern):
    if index >= len(pattern) - 1:
        return False
    top_index = index
    bottom_index = index + 1
    while top_index >= 0 and bottom_index < len(pattern):
        print("_________________________")
        print(pattern[top_index])
        print(pattern[bottom_index])
        print("_________________________")
        if pattern[top_index] != pattern[bottom_index]:
            return False
        top_index -= 1
        bottom_index += 1
    return True


def find_horizontal_value(pattern):
    for i, line in enumerate(pattern):
        if is_horizontal_reflection(i, pattern):
            return 100 * (i + 1)
    return 0


def is_vertical_reflection(index, pattern):
    if index >= len(pattern[0]) - 1:
        return False
    left_index = index
    right_index = index + 1
    while left_index >= 0 and right_index < len(pattern[0]):
        print(right_index)
        print(pattern[0])
        left_column = [row[left_index] for row in pattern]
        right_column = [row[right_index] for row in pattern]
        print("_________________")
        print(left_column)
        print(right_column)
        print("_________________")
        if left_column != right_column:
            return False
        left_index -= 1
        right_index += 1
    return True


def find_vertical_value(pattern):
    for i in range(len(pattern[0])):
        if is_vertical_reflection(i, pattern):
            return i + 1
    return 0


def find_total_value(patterns):
    print(patterns)
    vertical_val = 0
    horizontal_val = 0
    for i, pattern in enumerate(patterns):
        print(i)
        vertical_val += find_vertical_value(pattern)
        horizontal_val += find_horizontal_value(pattern)
    return vertical_val + horizontal_val


# print(patterns[-1])
# print(patterns[-1])
# print(find_total_value(patterns))


def find_smudge(pattern):
    horizontal_val = 0
    vertical_val = 0
    print(pattern)
    for i, row in enumerate(pattern):
        for j, col in enumerate(pattern[i]):
            # print(pattern)
            pattern[i].insert(j, "#" if pattern[i][j] == "." else ".")
            # print(pattern)
            # if is_horizontal_reflection(i - 1, pattern):
            #     horizontal_val += 100 * (i)
            # elif is_horizontal_reflection(i, pattern):
            #     horizontal_val += 100 * (i + 1)
            # elif is_vertical_reflection(j - 1, pattern):
            #     vertical_val += j
            # elif is_vertical_reflection(j, pattern):
            #     vertical_val += j + 1
            pattern[i].insert(j, "#" if pattern[i][j] == "." else ".")
            total = horizontal_val + vertical_val
            if total > 0:
                return total
    return horizontal_val + vertical_val


def find_smudges(patterns):
    total = 0
    # for pattern in patterns:
    find_smudge(patterns[0])
    return total


print(find_smudges(patterns[:1]))
