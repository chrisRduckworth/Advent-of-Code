def convert_hand_to_number(hand):
    """converts a hand to an integer so it can be compared in a sort"""
    """
    We will do this by creating a hex (because there are more than 10 
    cards).
    The first digit will be how high it ranks in terms of 5 of a kind
    vs 4 of a kind etc. Higher scoring hands have higher values
    Later digits will be equal to the value of each card, starting at the
    first
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

    return int(out_value, 16)

def total_winnings(games, part_2=False):
    games = {game.split()[0]: int(game.split()[1]) for game in games.splitlines()}
    hands = list(games.keys())
    if part_2:
        hands.sort(key=convert_hand_to_number_with_jokers)
    else:
        hands.sort(key=convert_hand_to_number)
    winnings = sum((i + 1) * games[hand] for i, hand in enumerate(hands))
    return winnings

def convert_hand_to_number_with_jokers(hand):
    number_of_jokers = hand.count("J")
    unique_cards = set(hand.replace("J", ""))
    if hand == "JJJJJ":
        highest_number_of_single_card = 0
    else:
        highest_number_of_single_card = max([hand.count(c) for c in unique_cards])
    # now account for jokers 
    highest_number_of_single_card += number_of_jokers

    if highest_number_of_single_card == 5:
        out_value = "7"
    elif highest_number_of_single_card == 4:
        out_value = "6"
    elif highest_number_of_single_card == 3:
        if len(unique_cards) == 2:
            # full house
            out_value = "5"
        else:
            # 3 of a kind
            out_value = "4"
    elif highest_number_of_single_card == 2:
        if len(unique_cards) == 3:
            # 2 pair
            out_value = "3"
        else:
            # 1 pair
            out_value = "2"
    else:
        out_value = "1"

    card_hex_values = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9":"9", "T": "A", "J": "1", "Q": "C", "K": "D", "A": "E"}

    for card in hand:
        out_value += card_hex_values[card]

    return int(out_value, 16)

if __name__ == "__main__":
    with open("inputs/day_7.txt") as f:
        games = f.read()
        winnings = total_winnings(games)
        print(winnings, "< total winnings")
        winnings_with_jokers = total_winnings(games, True)
        print(winnings_with_jokers, "< total winnings with jokers")
