from functools import cmp_to_key
from operator import itemgetter

CARD_RANKS = {
    "A": 12, "K": 11,
    "Q": 10, "T": 9,
    "9": 8,  "8": 7,
    "7": 6,  "6": 5,
    "5": 4,  "4": 3,
    "3": 2,  "2": 1,
    "J": 0,
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
        card_rank = CARD_RANKS[card]
        card_nums.setdefault(card_rank, 0)
        card_nums[card_rank] += 1
    
    # handle wildcards (J)
    if 0 in card_nums:
        num_jacks = card_nums[0]
        if num_jacks != 5: # stupid edge case: JJJJJ
            del card_nums[0]
            # sort by card type with largest qty, followed by rank
            card_to_mod = [c[0] for c in sorted(card_nums.items(), key=itemgetter(1, 0))][-1]
            card_nums[card_to_mod] += num_jacks
    
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
winnings = 0
for i in range(len(hands)):
    winnings += (i+1) * hands[i][1]

print(winnings)