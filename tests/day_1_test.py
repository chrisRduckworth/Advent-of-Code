from day_1 import sum_calibration_values
import pytest

class TestSumCalibrationValues:
    def test_sums_single_values(self):
        """calculates the sum when given a single value"""
        input_values = "1abc2"
        output = sum_calibration_values(input_values)
        assert output == 12

    def test_sums_single_digit(self):
        """calculates the sum when a single value with only one digit"""
        input_values = "treb7uchet"
        output = sum_calibration_values(input_values)
        assert output == 77

    def test_sums_multiple_values(self):
        """calculates the sum when passed multiple values"""
        input_values = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"
        output = sum_calibration_values(input_values)
        assert output == 142

    def test_replaces_words_with_digits(self):
        """replaces words with digits"""
        input_values = "two1nine"
        output = sum_calibration_values(input_values)
        assert output == 29

    def test_handles_overlap(self):
        """handles overlap of number names"""
        input_values = "eighthree"
        output = sum_calibration_values(input_values)
        assert output == 83
    
    def test_relaces_words_with_digits_multiple_values(self):
        """replaces words with digits across all values"""
        input_values = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
        output = sum_calibration_values(input_values)
        assert output == 281
        
