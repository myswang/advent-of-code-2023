from operator import itemgetter

'''
Replace face cards with hex.
Returns a valid hex string.
'''
def process_hand(hand: str):
    cards = "AKQJT"
    replacements = "EDCBA"
    for card, replacement in zip(cards, replacements):
        hand = hand.replace(card, replacement)
    return hand

'''
Gets the type of the hand.
Returns an integer from 0-6 (weakest-strongest)
'''
def get_hand_type(hand):
    hand_types = {
        (5,): 6, (1, 4): 5, (2, 3): 4, (1, 3): 3,
        (2, 2): 2, (1, 2): 1, (1, 1): 0
    }
    # count the number of cards of each type present
    card_nums = {}
    for card in hand:
        card_nums.setdefault(card, 0)
        card_nums[card] += 1
    
    # match hand to hand type
    card_nums = tuple(sorted(list(card_nums.values())))[-2:]
    return hand_types[card_nums]

# parse puzzle input
hands = []
with open("input.txt", "r") as input_file:
    for line in input_file.read().splitlines():
        hand, bid = line.split()
        hand = process_hand(hand)
        hands.append((hand, int(bid), get_hand_type(hand)))

# sort the hands, using custom compare_hands comparator
hands.sort(key=itemgetter(2, 0))

# compute the winnings
winnings = sum(idx * hand[1] for idx, hand in enumerate(hands, 1))
print(winnings)