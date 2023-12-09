from day_9 import find_subsequences, find_next_value, sum_extrapolated_values

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
