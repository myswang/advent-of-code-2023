import re

RED = r"\d+(?= red)"
GREEN = r"\d+(?= green)"
BLUE = r"\d+(?= blue)"

def find_max_cubes(colour, game):
    matches = re.findall(colour, game)
    return max([int(match) for match in matches])

# read puzzle input
with open("input.txt", "r") as input_file:
    lines = input_file.read().splitlines()

sum = 0
for line in lines:
    sum += find_max_cubes(RED, line) * find_max_cubes(GREEN, line) * find_max_cubes(BLUE, line)

print(sum)