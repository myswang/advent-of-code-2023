import re

# replacements for "digits"
word_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

# read puzzle input
with open("input.txt", "r") as input_file:
    lines = input_file.read().splitlines()

sum = 0
for line in lines:
    matches = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    first = matches[0]
    last = matches[-1]
    if not first.isdigit():
        first = word_to_digit[first]
    if not last.isdigit():
        last = word_to_digit[last]
    sum += int(first + last)
    
print(sum)