import re

def get_neighbours(xpos, span):
    neighbours = []
    for i in range(span[0]-1, span[1]+1):
        neighbours.append((xpos-1, i))
        neighbours.append((xpos+1, i))
    neighbours.append((xpos, span[0]-1))
    neighbours.append((xpos, span[1]))
    return neighbours

# read puzzle input
with open("input.txt", "r") as input_file:
    lines = input_file.read().splitlines()

number_matches = []

for line in lines:
    matches = re.finditer(r"\d+", line)
    number_matches.append([m.span() for m in matches])

sum = 0
for i in range(len(number_matches)):
    for match in number_matches[i]:
        neighbours = get_neighbours(i, match)
        for neighbour in neighbours:
            if (neighbour[0] < 0 or neighbour[1] < 0 or 
                    neighbour[0] > len(lines)-1 or 
                    neighbour[1] > len(lines[i])-1):
                continue
            cur_symbol = lines[neighbour[0]][neighbour[1]]
            if cur_symbol != "." and not cur_symbol.isnumeric():
                sum += int(lines[i][match[0]:match[1]])
                break
                
print(sum)


