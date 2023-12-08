from functools import cmp_to_key


values = 'AKQT98765432J'
values_ = 'AKQT98765432'

def get_type(hand):
    counts = sorted([hand.count(v) for v in values_], reverse=True)
    jokers = hand.count('J')
    counts[0] += jokers
    if counts[0] == 5:
        # Five of a kind
        return 0
    elif counts[0] == 4:
        # Four of a kind
        return 1
    elif counts[:2] == [3, 2]:
        # Full house
        return 2
    elif counts[0] == 3:
        # Three of a kind
        return 3
    elif counts[:2] == [2, 2]:
        # Two pairs
        return 4
    elif counts[0] == 2:
        # One pair
        return 5
    else:
        return 6

def cmp(a, b):
    hand_a, _ = a
    hand_b, _ = b

    type_a = get_type(hand_a)
    type_b = get_type(hand_b)

    if type_a < type_b:
        return -1
    elif type_a > type_b:
        return 1
    else:
        # Types are equal, so check pairs
        for a, b in zip(hand_a, hand_b):
            if values.index(a) < values.index(b):
                return -1
            elif values.index(a) > values.index(b):
                return 1

with open('test') as f:
    rounds = [line.split() for line in f.readlines()]

by_hand_value = sorted(rounds, key=cmp_to_key(cmp), reverse=True)
print(sum(int(x[1]) * (i + 1) for i, x in enumerate(by_hand_value)))
