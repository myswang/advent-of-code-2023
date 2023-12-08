import os
import re

input_dirname = os.path.dirname(__file__)
input_filename = os.path.join(input_dirname, "inputs/input.txt")
with open(input_filename, "r") as input_file:
    lines = input_file.read().splitlines()

instructions = [int(step) for step in lines[0].replace("R", " 1").replace("L", " 0").split()]

nodes = {}
for line in lines[2:]:
    matches = re.findall(r"\w\w\w", line)
    nodes[matches[0]] = tuple(matches[1:])

cur_node = "AAA"
num_steps = 0
done = False
while(True):
    for idx, instruction in enumerate(instructions, 1):
        if cur_node == "ZZZ":
            done = True
            break
        cur_node = nodes[cur_node][instruction]
    num_steps += idx
    if(done):
        num_steps -= 1
        break

print(num_steps)