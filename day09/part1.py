with open("input.txt", "r") as input_file:
    lines = input_file.read().splitlines()

report = ([int(num) for num in line.split()] for line in lines)

extrapolated_sum = 0
for sequence in report:
    sequence.append(sequence[-1])
    sequences = [sequence]
    while len(set(sequence)) > 1:
        sequences.append([0] * (len(sequence) - 1))
        for i in range(len(sequence) - 1):
            sequences[-1][i] = sequence[i+1] - sequence[i]
        sequences[-1][-1] = sequences[-1][-2]
        sequence = sequences[-1]
    for i in reversed(range(len(sequences) - 1)):
        sequences[i][-1] = sequences[i][-2] + sequences[i+1][-1]
    extrapolated_sum += sequences[0][-1]

print(extrapolated_sum)