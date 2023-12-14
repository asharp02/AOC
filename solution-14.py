from typing import List
    

class ReflectorDish:
    dish = []
    total_load = 0
    def __init__(self, filename) -> None:
        self.dish = self.parse_input_file(filename)
        for i in range(len(self.dish)):
            for j in range(len(self.dish[i])):
                self.move_north(i, j)
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
    
    def move_north(self, i, j):
        if i < 1 or self.dish[i][j] != "O":
            return
        if self.dish[i - 1][j] == ".":
            # move up recursively
            self.dish[i - 1][j] = "O"
            self.dish[i][j] = "."
            self.move_north(i - 1, j)
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
r2 = ReflectorDish("input.txt")
print(r.dish)
print(r.total_load)
print(r2.total_load)

