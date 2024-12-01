import re
from collections import Counter

with open("../inputs/01", "r") as f:
    lines = f.readlines()
    # Parse the two numbers in the lines using regex into a list of lists
    left_numbers, right_numbers = zip(*[re.findall(r"-?\d+", line) for line in lines])
    left_numbers = list(map(int, left_numbers))
    right_numbers = list(map(int, right_numbers))


total_distance = 0
for left, right in zip(sorted(left_numbers), sorted(right_numbers)):
    total_distance += abs(left - right)

print(total_distance)

similarity_score = 0
right_list_counts = Counter(right_numbers)
for left in left_numbers:
    similarity_score += right_list_counts[left] * left

print(similarity_score)
