from itertools import product
from collections import Counter

STRENGTH = [*map(str, range(2, 10)), "T", "J", "Q", "K", "A"]
STRENGTH_JOKER = ["J", *map(str, range(2, 10)), "T", "Q", "K", "A"]


class HandType:
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


def score_hand(hand: str) -> HandType:
    counts = Counter(hand)

    if max(counts.values()) == 5:
        return HandType.FIVE_OF_A_KIND

    if max(counts.values()) == 4:
        return HandType.FOUR_OF_A_KIND

    if 3 in counts.values() and 2 in counts.values():
        return HandType.FULL_HOUSE

    if max(counts.values()) == 3:
        return HandType.THREE_OF_A_KIND

    if list(counts.values()).count(2) == 2:
        return HandType.TWO_PAIR

    if 2 in counts.values():
        return HandType.ONE_PAIR

    return HandType.HIGH_CARD


def sort_key(hand):
    return score_hand(hand), *(STRENGTH.index(c) for c in hand)


def sort_key_joker(hand):
    joker_idx = [idx for idx, c in enumerate(hand) if c == "J"]

    max_score = score_hand(hand)
    for replacements in product(STRENGTH_JOKER[1:], repeat=len(joker_idx)):
        _hand = hand
        for idx, replacement in zip(joker_idx, replacements):
            _hand = _hand[:idx] + replacement + _hand[idx + 1 :]
            max_score = max(max_score, score_hand(_hand))

    return max_score, *(STRENGTH_JOKER.index(c) for c in hand)


def main():
    with open("../inputs/07", "r") as f:
        seq = f.read()
        lines = seq.split("\n")

    hands = []
    bids = {}
    for line in lines:
        hand, bid = line.split(" ")
        hands.append(hand)
        bids[hand] = int(bid)

    sorted_hands = sorted(hands, key=sort_key)

    s = sum([(rank + 1) * bids[hand] for rank, hand in enumerate(sorted_hands)])
    print(s)

    sorted_hands = sorted(hands, key=sort_key_joker)
    s = sum([(rank + 1) * bids[hand] for rank, hand in enumerate(sorted_hands)])
    print(s)


if __name__ == "__main__":
    main()
