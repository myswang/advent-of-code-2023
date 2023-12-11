# read puzzle input
with open("input.txt", "r") as input_file:
    blocks = input_file.read().split("\n\n")

# obtain the seeds
seeds = [int(b) for b in blocks[0].split()[1:]]

# parse the almanac maps
almanac = []
for block in blocks[1:]:
    temp = block.splitlines()[1:]
    alm_map = {}
    for mapping in temp:
        nums = [int(m) for m in mapping.split()]
        alm_map[(nums[1], nums[1]+nums[2]-1)] = nums[0] - nums[1]
    almanac.append(alm_map)

# apply the maps sequentially to each seed
res = []
for seed in seeds:
    for alm_map in almanac:
        for rag, dif in alm_map.items():
            if seed <= rag[1] and seed >= rag[0]:
                seed += dif
                break
    res.append(seed)

# return the min value
print(min(res))