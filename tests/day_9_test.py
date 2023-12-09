from day_9 import find_subsequences, find_next_value, sum_extrapolated_values, find_zero_value

class TestFindSubsequences:
    def test_returns_sequence_for_constant(self):
        sequence = [3, 3, 3, 3]

        subsequences = find_subsequences(sequence)

        assert subsequences == [[3, 3, 3, 3]]

    def test_returns_subsequences_for_linear(self):
        sequence = [0, 3, 6, 9, 12, 15]

        subsequences = find_subsequences(sequence)

        assert subsequences == [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3]]

    def test_returns_subsequences(self):
        sequence_1 = [1, 3, 6, 10, 15, 21]
        sequence_2 = [10, 13, 16, 21, 30, 45]
        
        subsequences_1 = find_subsequences(sequence_1)
        subsequences_2 = find_subsequences(sequence_2)

        assert subsequences_1 == [
                [1, 3, 6, 10, 15, 21],
                [2, 3, 4, 5, 6],
                [1, 1, 1, 1]
                ]
        assert subsequences_2 == [
                [10, 13, 16, 21, 30, 45],
                [3, 3, 5, 9, 15],
                [0, 2, 4, 6],
                [2, 2, 2]
                ]

class TestFindNextValue:
    def test_returns_number_for_constant(self):
        subsequences = [[3, 3, 3, 3]]

        next_value = find_next_value(subsequences)

        assert next_value == 3
    
    def test_returns_next_number_for_linear(self):
        subsequences = [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3]]

        next_value = find_next_value(subsequences)

        assert next_value == 18

    def test_returns_next_number(self):
        subsequences_1 = [
            [1, 3, 6, 10, 15, 21],
            [2, 3, 4, 5, 6],
            [1, 1, 1, 1]
            ]

        subsequences_2 = [
            [10, 13, 16, 21, 30, 45],
            [3, 3, 5, 9, 15],
            [0, 2, 4, 6],
            [2, 2, 2]
        ]

        next_value_1 = find_next_value(subsequences_1)
        next_value_2 = find_next_value(subsequences_2)

        assert next_value_1 == 28
        assert next_value_2 == 68

class TestSumExtrapolatedValues:
    def test_returns_sum_of_single_sequence(self):
        sequences_1 = "3   3   3   3  3  3"
        sequences_2 = "0   3   6   9  12  15"
        sequences_3 = "10 13 16 21 30 45"

        sums_1 = sum_extrapolated_values(sequences_1)
        sums_2 = sum_extrapolated_values(sequences_2)
        sums_3 = sum_extrapolated_values(sequences_3)

        assert sums_1 == 3
        assert sums_2 == 18
        assert sums_3 == 68
        
    def test_returns_sum_of_sequences(self):
        sequences = "0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45"

        sums = sum_extrapolated_values(sequences)

        assert sums == 114
        
class TestFindZeroValue:
    def test_returns_number_for_constant(self):
        subsequences = [[3, 3, 3, 3]]

        zero = find_zero_value(subsequences)

        assert zero == 3
    
    def test_returns_zero_number_for_linear(self):
        subsequences = [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3]]

        zero = find_zero_value(subsequences)

        assert zero == -3

    def test_returns_zero_number(self):
        subsequences_1 = [
            [1, 3, 6, 10, 15, 21],
            [2, 3, 4, 5, 6],
            [1, 1, 1, 1]
            ]

        subsequences_2 = [
            [10, 13, 16, 21, 30, 45],
            [3, 3, 5, 9, 15],
            [0, 2, 4, 6],
            [2, 2, 2]
        ]

        zero_1 = find_zero_value(subsequences_1)
        zero_2 = find_zero_value(subsequences_2)

        assert zero_1 == 0
        assert zero_2 == 5
