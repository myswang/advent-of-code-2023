from functools import cmp_to_key

RANKS = {
    "A": 12, "K": 11,
    "Q": 10, "J": 9,
    "T": 8,  "9": 7,
    "8": 6,  "7": 5,
    "6": 4,  "5": 3,
    "4": 2,  "3": 1,
    "2": 0,
}

def get_hand_type(hand):
    card_nums = {}
    for card in hand:
        card_nums.setdefault(card, 0)
        card_nums[card] += 1
    card_nums = tuple(sorted(list(card_nums.values())))
    match card_nums:
        case (5,):
            return 6 # five of a kind
        case (1, 4):
            return 5 # four of a kind
        case (2, 3):
            return 4 # full house
        case (1, 1, 3):
            return 3 # three of a kind
        case (1, 2, 2):
            return 2 # two pair
        case (1, 1, 1, 2):
            return 1 # pair
        case _:
            return 0 # high card

def compare_hands(hand1, hand2):
    if hand1[2] < hand2[2]:
        return -1
    elif hand1[2] > hand2[2]:
        return 1
    else:
        for h1, h2 in zip(hand1[0], hand2[0]):
            if RANKS[h1] < RANKS[h2]:
                return -1
            elif RANKS[h1] > RANKS[h2]:
                return 1
        return 0

with open("input.txt", "r") as input_file:
    hands = []
    for line in input_file.read().splitlines():
        hand, bid = line.split()
        hands.append((hand, int(bid), get_hand_type(hand)))

hands = sorted(hands, key=cmp_to_key(compare_hands))

winnings = 0
for i in range(len(hands)):
    winnings += (i+1) * hands[i][1]

print(winnings)