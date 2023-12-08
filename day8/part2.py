from collections import deque
from math import lcm
import os
import re

input_dirname = os.path.dirname(__file__)
input_filename = os.path.join(input_dirname, "inputs/input.txt")
with open(input_filename, "r") as input_file:
    lines = input_file.read().splitlines()

instructions = [int(step) for step in lines[0].replace("R", " 1").replace("L", " 0").split()]

node_map = {}
for line in lines[2:]:
    matches = re.findall(r"\w\w\w", line)
    node_map[matches[0]] = tuple(matches[1:])

starting_nodes = (node for node in node_map.keys() if node[-1] == "A")
result_steps = []
for node in starting_nodes:
    num_steps = 0
    instruct_queue = deque(instructions)
    while node[-1] != "Z":
        instruction = instruct_queue.popleft()
        node = node_map[node][instruction]
        num_steps += 1
        instruct_queue.append(instruction)
    result_steps.append(num_steps)

print(lcm(*result_steps))