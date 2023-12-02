from day_2 import sum_valid_games

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
