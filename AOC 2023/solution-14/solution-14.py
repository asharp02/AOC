from typing import List

import numpy as np


class ReflectorDish:
    dish = []
    total_load = 0

    def __init__(self, filename) -> None:
        self.dish = self.parse_input_file(filename)
        self.original_dish = [row.copy() for row in self.dish]
        print(self.original_dish)
        # print(self.dish)
        # print("________________")
        self.perform_cycles(1000)
        # if self.dish == self.original_dish:
        #     print(f"MATCH {i}")
        # self.perform_cycles(10)
        # self.calculate_load()
        # self.perform_cycles(100)
        # self.calculate_load()
        # self.perform_cycles(1000)
        # self.calculate_load()
        # self.perform_cycles(10000)
        # self.calculate_load()
        # self.perform_cycles(5)
        # self.calculate_load()
        # self.perform_cycles(6)
        # self.calculate_load()
        # self.perform_cycles(7)
        # self.calculate_load()
        # self.perform_cycles(8)
        # self.calculate_load()
        # self.perform_cycles(9)
        # self.calculate_load()
        # self.perform_cycles(10)
        # self.calculate_load()

        self.total_load = self.calculate_load()

    def perform_cycles(self, num_cycles):
        deltas_back = [(-1, 0), (0, -1)]
        deltas_forward = [(1, 0), (0, 1)]
        for n in range(num_cycles):
            for delta_x, delta_y in deltas_back:
                for i in range(len(self.dish)):
                    for j in range(len(self.dish[i])):
                        self.roll(i, j, delta_x, delta_y)
                # print(self.dish)
                # print("______________________")
            for delta_x, delta_y in deltas_forward:
                for i in range(len(self.dish) - 1, -1, -1):
                    for j in range(len(self.dish[i]) - 1, -1, -1):
                        self.roll(i, j, delta_x, delta_y)
                # print(self.dish)
                # print("______________________")

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
        print(total_load)
        return total_load


r = ReflectorDish("test-input.txt")
# r2 = ReflectorDish("input.txt")
# print(r.dish)
# print(r.total_load)
# print(r2.total_load)


class ReflectorDishNumpy:
    dish = []
    total_load = 0

    def __init__(self, filename) -> None:
        self.dish = self.parse_input_file(filename)
        print(self.dish)
        # self.original_dish = [row.copy() for row in self.dish]
        # print(self.original_dish)
        # print(self.dish)
        # print("________________")
        self.perform_cycles(1000)
        # if self.dish == self.original_dish:
        #     print(f"MATCH {i}")
        # self.perform_cycles(10)
        # self.calculate_load()
        # self.perform_cycles(100)
        # self.calculate_load()
        # self.perform_cycles(1000)
        # self.calculate_load()
        # self.perform_cycles(10000)
        # self.calculate_load()
        # self.perform_cycles(5)
        # self.calculate_load()
        # self.perform_cycles(6)
        # self.calculate_load()
        # self.perform_cycles(7)
        # self.calculate_load()
        # self.perform_cycles(8)
        # self.calculate_load()
        # self.perform_cycles(9)
        # self.calculate_load()
        # self.perform_cycles(10)
        # self.calculate_load()

        self.total_load = self.calculate_load()

    def perform_cycles(self, num_cycles):
        deltas_back = [(-1, 0), (0, -1)]
        deltas_forward = [(1, 0), (0, 1)]
        for n in range(num_cycles):
            for delta_x, delta_y in deltas_back:
                for i in range(len(self.dish)):
                    for j in range(len(self.dish[i])):
                        self.roll(i, j, delta_x, delta_y)
                # print(self.dish)
                # print("______________________")
            for delta_x, delta_y in deltas_forward:
                for i in range(len(self.dish) - 1, -1, -1):
                    for j in range(len(self.dish[i]) - 1, -1, -1):
                        self.roll(i, j, delta_x, delta_y)
                # print(self.dish)
                # print("______________________")

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
        return np.array(puzzle)

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
        print(total_load)
        return total_load


# r = ReflectorDishNumpy("test-input.txt")
