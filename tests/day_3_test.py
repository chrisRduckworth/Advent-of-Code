from day_3 import has_adjacent_symbol, sum_part_numbers
import pytest

class TestHasAdjacentSymbol:
    # need: works for start/end of row
    # detects adjacent symbol (including numbers)
    def test_detects_no_symbols(self):
        """returns false if no symbols are adjacent"""
        input_rows = [["...",".5.","..."]]

        output = has_adjacent_symbol(1, 1, input_rows)

        assert output == False

    def test_detects_adjacent_symbols(self):
        pass

    def test_detects_adjacent_numbers(self):
        pass

    def test_detects_diagonal_symbols(self):
        pass

    def test_start_index_zero(self):
        pass

    def test_start_index_at_the_end(self):
        pass
