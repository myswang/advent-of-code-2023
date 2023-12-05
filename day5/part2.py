def apply_map(seed_ranges, alm_map):
    res = set()
    while len(seed_ranges) > 0:
        sr = seed_ranges.pop()
        for rag, dif in alm_map.items():
            if sr[0] > rag[1] or sr[1] < rag[0]:
                continue
            if sr[1] > rag[1]:
                seed_ranges.append((rag[1]+1, sr[1]))
                sr = (sr[0], rag[1])
            if sr[0] < rag[0]:
                seed_ranges.append((sr[0], rag[0]-1))
                sr = (rag[0], sr[1])
            sr = (sr[0]+dif, sr[1]+dif)
            res.add(sr)
            break
        res.add(sr)
    return(list(res))

with open("input.txt", "r") as input_file:
    blocks = input_file.read().split("\n\n")

seeds = [int(b) for b in blocks[0].split()[1:]]
seed_ranges = []
for i in range(0,len(seeds),2):
    seed_ranges.append((seeds[i], seeds[i]+seeds[i+1]-1))

almanac = []
for block in blocks[1:]:
    temp = block.splitlines()[1:]
    alm_map = {}
    for mapping in temp:
        nums = [int(m) for m in mapping.split()]
        alm_map[(nums[1], nums[1]+nums[2]-1)] = nums[0] - nums[1]
    almanac.append(alm_map)

for alm_map in almanac:
    seed_ranges = apply_map(seed_ranges, alm_map)

print(min([sr[0] for sr in seed_ranges]))