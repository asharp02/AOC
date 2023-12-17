import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", action="store_true", help="run with test input")
args = parser.parse_args()


def parse_file(file_data):
    return [list(line) for line in file_data.splitlines()]


def rotate(parsed_data):
    pass


def part_2(parsed_data):
    for i in range(10):
        perform_cycle(parsed_data)


def perform_cycle(parsed_data):
    tilt_north(parsed_data)


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
        [row.count("O") * (len(parsed_data) - i) for i, row in enumerate(parsed_data)]
    )


if __name__ == "__main__":
    INPUT_FILE = "test-input.txt" if args.test else "input.txt"
    with open(INPUT_FILE, "r") as f:
        parsed_data = parse_file(f.read())
        print(part_1(parsed_data))
