def convert_hand_to_number(hand):
    """converts a hand to an integer so it can be compared in a sort"""
    """
    We will do this by creating a hex (because there are more than 10 
    cards).
    The first digit will be how high it ranks in terms of 5 of a kind
    vs 4 of a kind etc. Higher scoring hands have higher values
    """
    # test for various hands
    unique_cards = set(hand)
    if len(unique_cards) == 1:
        # 5 of a kind
        out_value = "7"
    elif len(unique_cards) == 2:
        if hand.count(list(unique_cards)[0]) in [1,4]:
            # 4 of a kind
            out_value = "6"
        else:
            # full house
            out_value = "5"
    elif len(unique_cards) == 3:
        if max([hand.count(c) for c in unique_cards]) == 3:
            # 3 of a kind
            out_value = "4"
        else:
            # 2 pair
            out_value = "3"
    elif len(unique_cards) == 4:
        # one pair
        out_value = "2"
    else:
        # high card 
        out_value = "1"

    card_hex_values = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9":"9", "T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

    for card in hand:
        out_value += card_hex_values[card]
    print(out_value)

    return int(out_value, 16)

def total_winnings(hands):
    pass
