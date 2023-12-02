from day_2 import sum_valid_games, sum_minimum_powers

class TestSumValidGames:
    def test_returns_sum_of_single_valid_game(self):
        games = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

        sum_of_games = sum_valid_games(games)

        assert sum_of_games == 1

    def test_returns_sum_of_single_invalid_game(self):
        games = "Game 1: 20 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        games_2 = "Game 1: 2 blue, 40 red; 1 red, 2 green, 6 blue; 2 green"
        games_3 = "Game 1: 2 blue, 4 red; 1 red, 20 green, 6 blue; 2 green"

        sum_of_games = sum_valid_games(games)
        sum_of_games_2 = sum_valid_games(games_2)
        sum_of_games_3 = sum_valid_games(games_3)

        assert sum_of_games == 0
        assert sum_of_games_2 == 0
        assert sum_of_games_3 == 0

    def test_returns_sum_of_multiple_valid_games(self):
        games = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 bluen\nGame 3: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"

        sum_of_games = sum_valid_games(games)

        assert sum_of_games == 6

    def test_returns_sum_of_multiple_invalid_games(self):
        games = "Game 1: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 2: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"

        sum_of_games = sum_valid_games(games)

        assert sum_of_games == 0

    def test_returns_sum_of_mixed_games(self):
        games = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"

        sum_of_games = sum_valid_games(games)

        assert sum_of_games == 8

class TestSumMinimumPowers:
    def test_returns_sum_powers_of_single_game(self):
        games = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        
        sum_of_minimum_powers = sum_minimum_powers(games)

        assert sum_of_minimum_powers == 48

    def test_returns_sum_powers_of_multiple_games(self):
        games = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"

        sum_of_minimum_powers = sum_minimum_powers(games)

        assert sum_of_minimum_powers == 2286
    
    def test_games_with_two_or_one_colours(self):
        games = "Game 1 : 3 blue; 2 red; 5 blue\nGame 2: 3 blue; 2 blue; 5 blue" 

        sum_of_minimum_powers = sum_minimum_powers(games)
        
        assert sum_of_minimum_powers == 15
    # need to test for games with only one/two colours
