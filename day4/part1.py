# read puzzle input
with open("input.txt", "r") as input_file:
    lines = input_file.read().splitlines()

sum = 0 
for line in lines:
    temp = line.split("|")
    win_nums = [int(i) for i in temp[0].split()[2:]]
    cur_nums = [int(i) for i in temp[1].split()]
    wins = set(win_nums) & set(cur_nums)
    sum += int(2 ** (len(wins)-1))

print(sum)