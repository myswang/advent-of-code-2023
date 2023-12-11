with open("input.txt", "r") as input_file:
    times, distances = [[int(num) for num in line.split()[1:]] for line in input_file.read().splitlines()]

num_wins = 0
for time, distance in zip(times, distances):
    cur_wins = 0
    for d in range(1, time):
        test_distance = d * (time - d)
        if test_distance > distance:
            cur_wins += 1
    if cur_wins != 0:
        if num_wins == 0:
            num_wins = cur_wins
        else:
            num_wins *= cur_wins

print(num_wins)