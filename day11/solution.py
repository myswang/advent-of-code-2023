# finds the row indexes where empty space is present
# returns a list of integers
def get_empty_space(universe):
    empty_space = "." * len(universe[0])
    return [idx for idx, line in enumerate(universe) if line == empty_space]

# counts the number of ints in spaces that are between min and max
# returns this count
def get_scale_factor(spaces, min, max):
    scale_factor = 0
    for space in spaces:
        if min <= space <= max:
            scale_factor += 1
    return scale_factor

# define universe expansion factors for part 1 and 2
expansion_factor1 = 1
expansion_factor2 = 999999

# read puzzle input
with open("input.txt", "r") as input_file:
    universe = input_file.read().splitlines()

# get indexes of empty spaces for rows and cols
empty_x = get_empty_space(universe)
empty_y = get_empty_space(["".join(s) for s in zip(*universe)])

# find the coordinates of all galaxies
galaxies = [(x, y) for x, line in enumerate(universe) for y, space in enumerate(line) if space == "#"]

# compute the distance of each galaxy from each other, using Manhattan distance
# scaled by the appropriate factor
len_sum1 = 0
len_sum2 = 0
for idx, p1 in enumerate(galaxies):
    for p2 in galaxies[idx+1:]:
        min_x, max_x = (p2[0], p1[0]) if p2[0] < p1[0] else (p1[0], p2[0])
        min_y, max_y = (p2[1], p1[1]) if p2[1] < p1[1] else (p1[1], p2[1])
        scale_factor = get_scale_factor(empty_x, min_x, max_x) + get_scale_factor(empty_y, min_y, max_y)
        dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        len_sum1 += dist + scale_factor * expansion_factor1
        len_sum2 += dist + scale_factor * expansion_factor2

print("Part 1 solution:", len_sum1)
print("Part 2 solution:", len_sum2)