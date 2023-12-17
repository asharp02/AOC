import argparse
import numpy as np
from collections import OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument("--test", action="store_true", help="run with test input")
args = parser.parse_args()


def parse_file(file_data):
    return [
        [list(row) for row in grid.splitlines()] for grid in file_data.split("\n\n")
    ]


def part_1(data):
    total_sum = 0
    for pattern in data:
        horizontal_line = check_horizontal(pattern)
        vertical_line = check_vertical(pattern)
        total_sum += horizontal_line * 100 + vertical_line
    return total_sum


def check_vertical(pattern):
    rotated = np.rot90(pattern, -1)
    return check_horizontal(rotated)


def check_horizontal(pattern):
    for i in range(len(pattern) - 1):
        if is_reflection_line(pattern, i, i + 1) == True:
            return i + 1
    return 0


def is_reflection_line(pattern, row_a, row_b):
    if row_a < 0 or row_b >= len(pattern):
        return True
    if tuple(pattern[row_a]) != tuple(pattern[row_b]):
        return False
    return is_reflection_line(pattern, row_a - 1, row_b + 1)


def part_2(data):
    pass


if __name__ == "__main__":
    INPUT_FILE = "test-input.txt" if args.test else "input.txt"
    with open(INPUT_FILE, "r") as f:
        parsed_data = parse_file(f.read())
        print(part_1(parsed_data))
        # part_2(parsed_data)
