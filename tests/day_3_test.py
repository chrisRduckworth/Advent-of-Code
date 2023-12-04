from day_3 import has_adjacent_symbol, sum_part_numbers, find_gear_ratio, sum_gear_ratios
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

class TestSumPartNumbers:
    def test_sums_numbers_with_adjacent_symbols(self):
        schematic = "467..1\n@..5.~\n1.&..."

        output = sum_part_numbers(schematic)

        assert output == 474

    def test_ignores_numbers_with_no_symbols(self):
        schematic = "467..1\n......\n1.5..."

        output = sum_part_numbers(schematic)

        assert output == 0
    
    def test_mixed_numbers(self):
        schematic = "467..114..\n...*......\n..35..633.\n......@...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.."

        output = sum_part_numbers(schematic)
        
        assert output == 4361

class TestFindGearRatio:
    def test_returns_0_for_no_adjacent_numbers(self):
        input_rows = ["...", ".*.", "..."]
        
        output = find_gear_ratio(1, input_rows)

        assert output == 0

    def test_returns_0_for_one_adjacent_number(self):
        input_rows = ["...", ".*5", "..."]

        output = find_gear_ratio(1, input_rows)

        assert output == 0

    def test_returns_0_for_3_or_more_adjacent_numbers(self):
        input_rows = ["5.5", ".*.", ".5."]

        output = find_gear_ratio(1, input_rows)

        assert output == 0

    def test_returns_gear_ratio_for_numbers_above(self):
        input_rows = ["5.6", ".*.", "..."]
        
        output = find_gear_ratio(1, input_rows)

        assert output == 30

    def test_returns_gear_ratio_for_numbers_to_side(self):
        input_rows = ["...", "5*6", "..."]
        
        output = find_gear_ratio(1, input_rows)

        assert output == 30

    def test_returns_gear_ratio_for_numbers_below(self):
        input_rows = ["...", ".*.", "5.6"]
        
        output = find_gear_ratio(1, input_rows)

        assert output == 30

    def test_returns_gear_ratio_for_numbers_mixed(self):
        input_rows = ["5..", "6*.", "..."]
        input_rows_2 = ["5..", "6*.", "..."]
        input_rows_3 = ["555", ".*.", ".6."]
        input_rows_4 = ["...", ".*6", "6.."]
        input_rows_5 = ["12345.", "..*..", ".12345"]
        
        output = find_gear_ratio(1, input_rows)
        output_2 = find_gear_ratio(1, input_rows_2)
        output_3 = find_gear_ratio(1, input_rows_3)
        output_4 = find_gear_ratio(1, input_rows_4)
        output_5 = find_gear_ratio(1, input_rows_5)

        assert output == 30
        assert output_2 == 30
        assert output_3 == 3330
        assert output_4 == 36
        assert output_5 == 152399025
    
    def test_returns_gear_ratio_for_gears_at_end_of_line(self):
        input_rows = ["5..", "*6.", "..."]
        input_rows_2 = ["..6", "..*", "555"]

        output = find_gear_ratio(0, input_rows)
        output_2 = find_gear_ratio(2, input_rows_2)

        assert output == 30
        assert output_2 == 3330

class TestSumGearRatios:
    def test_sums_gear_ratios(self):
        # it's midnight these are the only tests im writign for now
        schematic = "467..114..\n...*......\n..35..633.\n......@...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.."

        output = sum_gear_ratios(schematic)

        assert output == 467835
