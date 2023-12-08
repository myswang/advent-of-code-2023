from collections import deque
import os
import re

input_dirname = os.path.dirname(__file__)
input_filename = os.path.join(input_dirname, "inputs/input.txt")
with open(input_filename, "r") as input_file:
    lines = input_file.read().splitlines()

instructions = deque(int(step) for step in lines[0].replace("R", " 1").replace("L", " 0").split())

node_map = {}
for line in lines[2:]:
    matches = re.findall(r"\w\w\w", line)
    node_map[matches[0]] = tuple(matches[1:])

cur_node = "AAA"
num_steps = 0
while cur_node != "ZZZ":
    instruction = instructions.popleft()
    cur_node = node_map[cur_node][instruction]
    num_steps += 1
    instructions.append(instruction)

print(num_steps)