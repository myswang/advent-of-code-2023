from functools import cmp_to_key

CARD_RANKS = {
    "A": 12, "K": 11,
    "Q": 10, "J": 9,
    "T": 8,  "9": 7,
    "8": 6,  "7": 5,
    "6": 4,  "5": 3,
    "4": 2,  "3": 1,
    "2": 0,
}

HAND_TYPES = {
    (5,): 6,
    (1, 4): 5,
    (2, 3): 4,
    (1, 1, 3): 3,
    (1, 2, 2): 2,
    (1, 1, 1, 2): 1,
    (1, 1, 1, 1, 1): 0
}

'''
Gets the type of the hand.
Returns an integer from 0-6 (weakest-strongest)
'''
def get_hand_type(hand):
    # count the number of cards of each type present
    card_nums = {}
    for card in hand:
        card_nums.setdefault(card, 0)
        card_nums[card] += 1

    # match hand to hand type
    card_nums = tuple(sorted(list(card_nums.values())))
    return HAND_TYPES[card_nums]

'''
Compares two different hands.
hand1 and hand2 are tuples consisting of:
 - hand as string (i.e. 84J22)
 - bet
 - hand type, computed by the get_hand_type function
'''
def compare_hands(hand1, hand2):
    # compare hand type ranks
    if hand1[2] < hand2[2]:
        return -1
    if hand1[2] > hand2[2]:
        return 1
    for h1, h2 in zip(hand1[0], hand2[0]):
        if CARD_RANKS[h1] < CARD_RANKS[h2]:
            return -1
        if CARD_RANKS[h1] > CARD_RANKS[h2]:
            return 1
    return 0

# parse puzzle input
with open("input.txt", "r") as input_file:
    hands = []
    for line in input_file.read().splitlines():
        hand, bid = line.split()
        hands.append((hand, int(bid), get_hand_type(hand)))

# sort the hands, using custom compare_hands comparator
hands.sort(key=cmp_to_key(compare_hands))

# compute the winnings
winnings = sum(idx * hand[1] for idx, hand in enumerate(hands, 1))
print(winnings)