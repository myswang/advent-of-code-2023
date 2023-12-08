from math import lcm
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

starting_nodes = [node for node in nodes.keys() if node[-1] == "A"]
result_steps = []
done = False

for node in starting_nodes:
    num_steps = 0
    while(True):
        for instruction in instructions:
            if node[-1] == "Z":
                done = True
                break
            node = nodes[node][instruction]
            num_steps += 1
        if(done):
            break
    done = False
    result_steps.append(num_steps)

print(lcm(*result_steps))