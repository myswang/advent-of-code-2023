# read puzzle input
with open("input.txt", "r") as input_file:
    lines = input_file.read().splitlines()

# precompute the qty of winning numbers for each card
card_wins = []
for line in lines:
    temp = line.split("|")
    win_nums = [int(i) for i in temp[0].split()[2:]]
    cur_nums = [int(i) for i in temp[1].split()]
    wins = set(win_nums) & set(cur_nums)
    card_wins.append(len(wins))

card_nums = [1] * len(card_wins)
for i in range(len(card_wins)):
    for j in range(card_wins[i]):
        card_nums[i+j+1] += card_nums[i]

print(sum(card_nums))
