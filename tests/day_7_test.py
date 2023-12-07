from day_7 import convert_hand_to_number, total_winnings

class TestConvertHandToNumber:
    def test_returns_a_number(self):
        hand = "32T3K"

        value = convert_hand_to_number(hand)
        
        assert isinstance(value, int)

    def test_numbers_with_higher_score_return_higher_number(self):
        hand_1 = "32T3K"
        hand_2 = "T55J5"
        hand_3 = "KK677"
        hand_4 = "KTJJT"
        hand_5 = "QQQJA"
        hand_6 = "QQQQQ"
        hand_7 = "TTT7T"
        hand_8 = "TJTJT"
        hand_9 = "JTJTJ"
        hand_10 = "23456"
        hand_11 = "62345"

        value_1 = convert_hand_to_number(hand_1)
        value_2 = convert_hand_to_number(hand_2)
        value_3 = convert_hand_to_number(hand_3)
        value_4 = convert_hand_to_number(hand_4)
        value_5 = convert_hand_to_number(hand_5)
        value_6 = convert_hand_to_number(hand_6)
        value_7 = convert_hand_to_number(hand_7)
        value_8 = convert_hand_to_number(hand_8)
        value_9 = convert_hand_to_number(hand_9)
        value_10 = convert_hand_to_number(hand_10)
        value_11 = convert_hand_to_number(hand_11)

        assert value_6 > value_7
        assert value_7 > value_9
        assert value_9 > value_8
        assert value_8 > value_2
        assert value_2 > value_3
        assert value_3 > value_4
        assert value_4 > value_1
        assert value_1 > value_11
        assert value_11 > value_10

class TestTotalWinnings:
    def test_returns_total_for_one_hand(self):
        hands = "32T3K 765"

        winnings = total_winnings(hands)

        assert winnings == 765

    def test_returns_total_for_multiple_hands(self):
        hands = "32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483"

        winnings = total_winnings(hands)
        
        assert winnings == 6440
