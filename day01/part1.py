import re

# read puzzle input
with open("input.txt", "r") as input_file:
    lines = input_file.read().splitlines()

sum = 0
for line in lines:
    matches = re.findall(r'\d', line)
    sum += int(matches[0] + matches[-1])
    
print(sum)