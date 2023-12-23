hands = []
bids = []

cards = {
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14
}

with open("input.txt", "r+") as f:
    for line in f:
        l_i = line.strip().split(" ")
        hands.append(l_i[0])
        bids.append(int(l_i[1]))

def hand_rank(hand):
    hand_dict = dict()

    for card in hand:
        if hand_dict.get(card):
            hand_dict[card] += 1
        else:
            hand_dict[card] = 1
    values = list(hand_dict.values())
    values.sort(reverse=True)

    if values[0] == 5:
        return 6
    elif values[0] == 4:
        return 5
    elif values[0] == 3:
        if values[1] == 2:
            return 4
        return 3
    elif values[0] == 2:
        if values[1] == 2:
            return 2
        return 1
    else:
        return 0

def is_hand_greater_than(hand_1, hand_2):
    if hand_rank(hand_1) == hand_rank(hand_2):
        for c_1, c_2 in zip(hand_1,hand_2):
            if cards.get(c_1) > cards.get(c_2):
                return True
            elif cards.get(c_1) < cards.get(c_2):
                return False

    return hand_rank(hand_1) > hand_rank(hand_2)

#sorting the hands and bids
for c_1 in range(len(hands)):
    sm = c_1
    for c_2 in range(c_1, len(hands)):
        if is_hand_greater_than(hands[sm], hands[c_2]):
            sm = c_2

    card_holder = hands[c_1]
    hands[c_1] = hands[sm]
    hands[sm] = card_holder

    bids_holder = bids[c_1]
    bids[c_1] = bids[sm]
    bids[sm] = bids_holder

result = 0
for b in range(len(bids)):
    result += (b+1) * bids[b]

print(result)