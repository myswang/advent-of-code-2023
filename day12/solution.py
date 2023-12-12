import re

def check_springs(springs, groups):
    test_groups = tuple(len(match) for match in re.findall(r"#+", springs))
    nums_identical = True if test_groups == groups else False
    sums_identical = True if sum(test_groups) == sum(groups) else False
    return (nums_identical, sums_identical)

def dfs(springs, groups):
    memo = set()
    count = 0
    stack = [springs]
    while stack:
        cur_springs = stack.pop()
        if cur_springs in memo:
            continue
        nums_identical, sums_identical = check_springs(cur_springs, groups)
        if nums_identical:
            count += 1
        elif not sums_identical:
            open_slots = (match.span() for match in re.finditer(r"\?", cur_springs))
            for s1, s2 in open_slots:
                stack.append(cur_springs[:s1] + "#" + cur_springs[s2:])
        memo.add(cur_springs)
    return count
        

with open("input_sample.txt", "r") as input_file:
    lines = [line.split() for line in input_file.read().splitlines()]

counts1 = 0
counts2 = 0

for springs, groups in lines:
    groups = tuple(int(i) for i in groups.split(","))
    print(springs, groups)
    count = dfs(springs, groups)
    print(count)
    counts1 += count

# for springs, groups in lines:
#     springs = "?".join([springs] * 5)
#     groups = ",".join([groups] * 5)
#     groups = tuple(int(i) for i in groups.split(","))
#     print(springs, groups)
#     count = dfs(springs, groups)
#     print(count)
#     counts2 += count

print("Part 1 solution:", counts1)
print("Part 2 solution:", counts2)
