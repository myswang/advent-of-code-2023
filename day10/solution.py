import os

# openings for each pipe, (row, col) offsets 
pipe_openings = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1)),
}

# load the input file
input_dirname = os.path.dirname(__file__)
input_filename = os.path.join(input_dirname, "inputs/input.txt")
with open(input_filename, "r") as input_file:
    pipes = input_file.read().splitlines()

# find the starting point
for x0, row in enumerate(pipes):
    y0 = row.find("S")
    if y0 != -1:
        break

# replace the starting point "S" with the appropriate pipe
replace_value = ""
if pipes[x0-1][y0] in "|7F" and pipes[x0+1][y0] in "|JL":
    replace_value = "|"
elif pipes[x0-1][y0] in "|7F" and pipes[x0][y0-1] in "-FL":
    replace_value = "J"
elif pipes[x0-1][y0] in "|7F" and pipes[x0][y0+1] in "-7J":
    replace_value = "L"
elif pipes[x0+1][y0] in "|JL" and pipes[x0][y0-1] in "-FL":
    replace_value = "7"
elif pipes[x0+1][y0] in "|JL" and pipes[x0][y0+1] in "-7J":
    replace_value = "F"
else:
    replace_value = "-"
pipes[x0] = pipes[x0].replace("S", replace_value)

# setup a clean pipe diagram to remove trash pipes
pipes_clean = [["." for _ in range(len(pipes[0]))] for _ in range(len(pipes))]
# initialize distance and direction
direction = pipe_openings[replace_value][0]
distance = 0
x, y = x0, y0
while x != x0 or y != y0 or distance == 0:
    # get the pipe at (x, y) and add it to the clean pipe diagram
    pipe = pipes[x][y]
    pipes_clean[x][y] = pipe
    opening1, opening2 = pipe_openings[pipe]
    # obtain the direction opposite to the current direction , to avoid going backwards
    # then pick the direction that does not equal the opposite
    opposite = tuple(i * -1 for i in direction)
    direction = opening2 if opposite == opening1 else opening1
    x += direction[0]
    y += direction[1]
    distance += 1

# perform a scan across each line to look for enclosed tiles
# "open" tracks whether we are in the loop or not
# many conditionals are needed to handle edge cases
# edge case 1: ...(out loop)...F---J...(in loop)... (or L---7)
# edge case 2: ...(out loop)...F---7...(out loop)... (or L---J)
area = 0
for row in pipes_clean:
    open = -1
    prev = ""
    for pipe in row:
        if pipe == "|":
            open *= -1
        elif pipe == "." and open == 1:
            area += 1
        elif pipe in "FL":
            open *= -1
            prev = pipe
        elif pipe in "J7":
            if prev + pipe in "LJF7":
                open *= -1
            prev = ""
        else:
            continue

print("Part 1 solution:", distance // 2)
print("Part 2 solution:", area)