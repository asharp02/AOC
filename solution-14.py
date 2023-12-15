from typing import List


class ReflectorDish:
    dish = []
    total_load = 0

    def __init__(self, filename) -> None:
        self.dish = self.parse_input_file(filename)
        print(self.dish)
        print("________________")
        deltas_back = [(-1, 0), (0, -1)]
        deltas_forward = [(1, 0), (0, 1)]
        for delta_x, delta_y in deltas_back:
            for i in range(len(self.dish)):
                for j in range(len(self.dish[i])):
                    self.roll(i, j, delta_x, delta_y)
            print(self.dish)
            print("______________________")
        for delta_x, delta_y in deltas_forward:
            for i in range(len(self.dish) - 1, 0, -1):
                for j in range(len(self.dish[i]) - 1, 0, -1):
                    self.roll(i, j, delta_x, delta_y)
            print(self.dish)
            print("______________________")

        self.total_load = self.calculate_load()

    @staticmethod
    def parse_input_file(filename) -> List[List]:
        puzzle = []
        with open(filename) as file:
            for line in file:
                puzzle_row = []
                for char in line:
                    if char != "\n":
                        puzzle_row.append(char)
                puzzle.append(puzzle_row)
        return puzzle

    def roll(self, i, j, delta_i, delta_j):
        row_inbounds = 0 <= i < len(self.dish)
        col_inbounds = 0 <= j < len(self.dish[0])
        if not row_inbounds or not col_inbounds or self.dish[i][j] != "O":
            return
        new_row = i + delta_i
        new_col = j + delta_j
        delta_row_inbounds = 0 <= new_row < len(self.dish)
        delta_col_inbounds = 0 <= new_col < len(self.dish[0])
        if (
            delta_row_inbounds
            and delta_col_inbounds
            and self.dish[new_row][new_col] == "."
        ):
            # move up recursively
            self.dish[new_row][new_col] = "O"
            self.dish[i][j] = "."
            self.roll(new_row, new_col, delta_i, delta_j)
        return

    def calculate_load(self):
        level = len(self.dish)
        total_load = 0
        for i in range(len(self.dish)):
            for j in range(len(self.dish[i])):
                if self.dish[i][j] == "O":
                    total_load += level
            level -= 1
        return total_load


r = ReflectorDish("test-input.txt")
# r2 = ReflectorDish("input.txt")
print(r.dish)
print(r.total_load)
# print(r2.total_load)
