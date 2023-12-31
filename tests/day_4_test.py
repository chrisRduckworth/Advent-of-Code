from day_4 import sum_scratchcard_points, find_total_scratchcards

class TestSumScratchCards:
    def test_returns_zero_for_no_matching_numbers(self):
        scratchcards = "Card 1: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"

        points = sum_scratchcard_points(scratchcards)

        assert points == 0

    def test_single_match_worth_one(self):
        scratchcards = "Card 1: 41 92 73 84 69 | 59 84 76 51 58  5 54 83"
        
        points = sum_scratchcard_points(scratchcards)

        assert points == 1

    def test_multiple_matches_double(self):
        scratchcards = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        
        points = sum_scratchcard_points(scratchcards)

        assert points == 8

    def test_sums_several_cards(self):
        scratchcards = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"

        points = sum_scratchcard_points(scratchcards)

        assert points == 13

class TestFindTotalScratchcards:
    def test_no_winning_numbers(self):
        scratchcards = "Card 1: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 2: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"

        total_cards = find_total_scratchcards(scratchcards)

        assert total_cards == 2

    def test_winning_numbers(self):
        scratchcards = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"

        total_cards = find_total_scratchcards(scratchcards)

        assert total_cards == 30

    def test_last_card_has_winning_numbers(self):
        scratchcards = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"

        total_cards = find_total_scratchcards(scratchcards)

        assert total_cards == 3
        pass
