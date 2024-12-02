f = open("input.txt", "r")
left, right = [], []
for line in f.read().splitlines():
    left_val, right_val = line.split("   ")
    left.append(int(left_val))
    right.append(int(right_val))

##### PART 1 ######
left.sort()
right.sort()
running_total = 0
for i in range(len(left)):
    running_total += abs(left[i] - right[i])
print(running_total)

##### PART 2 ######
from collections import Counter

right_counts = Counter(right)
running_sim_score = 0
for num in left:
    running_sim_score += num * right_counts[num]
print(running_sim_score)
