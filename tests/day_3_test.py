from day_3 import has_adjacent_symbol, sum_part_numbers
import pytest

class TestHasAdjacentSymbol:
    def test_detects_no_symbols(self):
        """returns false if no symbols are adjacent"""
        input_rows = ["...",".5.","..."]

        output = has_adjacent_symbol(1, 1, input_rows)

        assert output == False

    def test_detects_adjacent_symbols(self):
        """returns true if there is an adjacent symbol"""
        input_rows = [".@.",".5.","..."]
        input_rows_2 = ["...","~5.","..."]
        input_rows_3 = ["...",".5.",".[."]
        input_rows_4 = ["...",".5a","..."]

        output = has_adjacent_symbol(1, 1, input_rows)
        output_2 = has_adjacent_symbol(1, 1, input_rows_2)
        output_3 = has_adjacent_symbol(1, 1, input_rows_3)
        output_4 = has_adjacent_symbol(1, 1, input_rows_4)

        assert output == True
        assert output_2 == True
        assert output_3 == True
        assert output_4 == True

    def test_detects_adjacent_numbers(self):
        """returns true if there is an adjacent number (above/below)"""
        input_rows = [".5.",".5.","..."]
        input_rows_2 = ["...",".5.",".5."]

        output = has_adjacent_symbol(1, 1, input_rows)
        output_2 = has_adjacent_symbol(1, 1, input_rows_2)

        assert output == True
        assert output_2 == True

    def test_detects_diagonal_symbols(self):
        """returns true if there is a number/symbol diagonally adjacent"""
        input_rows = ["@..",".5.","..."]
        input_rows_2 = ["..~",".5.","..."]
        input_rows_3 = ["...",".5.","[.."]
        input_rows_4 = ["...",".5.","..5"]

        output = has_adjacent_symbol(1, 1, input_rows)
        output_2 = has_adjacent_symbol(1, 1, input_rows_2)
        output_3 = has_adjacent_symbol(1, 1, input_rows_3)
        output_4 = has_adjacent_symbol(1, 1, input_rows_4)

        assert output == True
        assert output_2 == True
        assert output_3 == True
        assert output_4 == True

    def test_start_index_zero(self):
        """compensates for numbers start at the beginning of the row"""
        input_rows = [".....","5..55","....."]
        input_rows_2 = ["@.@..","5..55", "....."]
        
        output = has_adjacent_symbol(0, 1, input_rows)
        output_2 = has_adjacent_symbol(0, 1, input_rows_2)

        assert output == False
        assert output_2 == True

    def test_start_index_at_the_end(self):
        """compensates for numbers ending at the end of the row"""
        input_rows = [".....","5..55","....."]
        input_rows_2 = ["@.@..","5..55", "....."]
        
        output = has_adjacent_symbol(3, 2, input_rows)
        output_2 = has_adjacent_symbol(3, 2, input_rows_2)

        assert output == False
        assert output_2 == True
