from day_6 import find_winning_products

class TestFindWinningProducts:
    def test_returns_value_for_single_race(self):
        races = "Time:      7\nDistance:  9"

        winning_times = find_winning_products(races)

        assert winning_times == 4

    def test_returns_value_for_multiple_races(self):
        races = "Time:      7  15   30\nDistance:  9  40  200"

        product = find_winning_products(races)

        assert product == 288
