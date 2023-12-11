import math

with open("input.txt", "r") as input_file:
    time, distance = [int("".join(line.split()[1:])) for line in input_file.read().splitlines()]

lo = math.ceil((time - math.sqrt(time ** 2 - 4 * distance)) / 2)
hi = math.ceil((time + math.sqrt(time ** 2 - 4 * distance)) / 2)

print(hi - lo)
