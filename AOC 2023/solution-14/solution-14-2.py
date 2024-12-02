import argparse
import numpy as np
from collections import OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument("--test", action="store_true", help="run with test input")
args = parser.parse_args()


def parse_file(file_data):
    return [list(line) for line in file_data.splitlines()]


def part_2(data):
    data = np.array(data)
    grids_seen = {}
    repeat_loads_seen = []  # keep track of loads already seen to find a repeat

    # perform a cycle enough times to recognize a pattern amongst loads
    for i in range(400):
        perform_cycle(data)

        grid = tuple([tuple(row) for row in data])  # must convert grid to hashable type

        # keep track of grids already seen in dict
        if not grid in grids_seen:
            grids_seen[grid] = i
            continue

        # get load of current cycle's grid, only if grid has already been seen!
        load = calculate_load(grid)

        if repeat_loads_seen and load == repeat_loads_seen[0][0]:
            # we have returned back to the start of the load pattern
            # we can now analyze the pattern via loads_seen
            # NOTE: this does not work for patterns with repeated loads within them since it only finds a pattern
            # based on the first match and not the more than one load value
            break

        repeat_loads_seen.append((load, i))


def find_load_after_n_cycles(n, repeat_loads_seen):
    # take target cycle N, subtract number of iterations it takes to get to the first repeated grid from N
    print(repeat_loads_seen[0][1])
    target_n = n - repeat_loads_seen[0][1]

    # (N % len(repeat_loads_seen) - 1) should give you the index of the cycle's load within the repeat_loads_seen
    index_of_nth_load = (target_n % len(repeat_loads_seen)) - 1
    return repeat_loads_seen[index_of_nth_load][0]


def perform_cycle(data):
    tilt_north(data)

    # tilt west
    data = np.rot90(data, -1)
    tilt_north(data)
    data = np.rot90(data, 1)

    # tilt south
    data = np.rot90(data, k=2)
    tilt_north(data)
    data = np.rot90(data, k=2)

    # tilt east
    data = np.rot90(data, 1)
    tilt_north(data)
    data = np.rot90(data, -1)


def part_1(parsed_data):
    tilt_north(parsed_data)
    return calculate_load(parsed_data)


def tilt_north(parsed_data):
    # store the highest occupied row for each column in grid
    highest_occupied = {i: -1 for i in range(len(parsed_data[0]))}
    for i in range(len(parsed_data)):
        for j in range(len(parsed_data[i])):
            char = parsed_data[i][j]
            if char == "O":
                # check for the highest occupied row within curr col
                # if more than two rows above, replace following row with "O"
                if highest_occupied[j] + 1 != i:
                    parsed_data[highest_occupied[j] + 1][j] = "O"
                    parsed_data[i][j] = "."
                    highest_occupied[j] += 1
            # update highest occupied hash if curr index is occupied
            if parsed_data[i][j] != ".":
                highest_occupied[j] = i


def calculate_load(parsed_data):
    return sum(
        [
            list(row).count("O") * (len(parsed_data) - i)
            for i, row in enumerate(parsed_data)
        ]
    )


if __name__ == "__main__":
    INPUT_FILE = "test-input.txt" if args.test else "input.txt"
    with open(INPUT_FILE, "r") as f:
        parsed_data = parse_file(f.read())
        part_1(parsed_data)
        part_2(parsed_data)
