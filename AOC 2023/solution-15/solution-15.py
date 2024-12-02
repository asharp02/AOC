
class LensLibrary:

    sequence = []
    def __init__(self, filename):
        self.parse_input_file(filename)
        self.calculate_sum()

    def calculate_sum(self):
        total = 0
        for step in self.sequence:
            total += self.get_hash_value(step)
        print(total)
        return total

    def parse_input_file(self, filename):
        with open(filename) as f:
            for line in f:
                self.sequence = line.split(",")

    def get_hash_value(self, step):
        value = 0
        for char in step:
            value += ord(char)
            value *= 17
            value %= 256
        return value

l = LensLibrary("test-input.txt")
l = LensLibrary("input.txt")

