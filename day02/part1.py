import re

RED = (12, r"\d+(?= red)")
GREEN = (13, r"\d+(?= green)")
BLUE = (14, r"\d+(?= blue)")

def check_colour(colour, game):
    matches = re.findall(colour[1], game)
    for match in matches:
        if int(match) > colour[0]:
            return False
    return True

# read puzzle input
with open("input.txt", "r") as input_file:
    lines = input_file.read().splitlines()

sum = 0
for line in lines:
    if check_colour(RED, line) and check_colour(GREEN, line) and check_colour(BLUE, line):
        sum += int(re.search(r"\d+", line).group())

print(sum)