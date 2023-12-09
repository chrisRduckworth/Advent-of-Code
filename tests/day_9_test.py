from day_9 import find_subsequences, sum_extrapolated_values

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
