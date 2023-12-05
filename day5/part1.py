with open("input_sample.txt", "r") as input_file:
    blocks = input_file.read().split("\n\n")

# seeds = [int(b) for b in blocks[0].split()[1:]]
seeds = list(range(55, 68)) + list(range(79, 93))
print(seeds)

almanac = []

for block in blocks[1:]:
    temp = block.splitlines()[1:]
    alm_map = {}
    for mapping in temp:
        nums = [int(m) for m in mapping.split()]
        alm_map[(nums[1], nums[1]+nums[2]-1)] = nums[0] - nums[1]
    almanac.append(alm_map)
    print(alm_map)

res = []
for seed in seeds:
    for alm_map in almanac:
        for rag, dif in alm_map.items():
            if seed <= rag[1] and seed >= rag[0]:
                seed += dif
                break
    res.append(seed)

print(res)
print(min(res))
# only consider lowest number in every range
