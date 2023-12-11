from day_11 import expand_space, sum_shortest_distances

class TestExpandSpace:
    def returns_input_if_no_empty_space(self):
        image = ["#..", ".#.", "..#"]

        expanded_space = expand_space(image)

        assert expanded_space == ["#..", ".#.", "..#"]

    def expands_rows(self):
        pass

    def expands_columns(self):
        pass

    def expands_rows_and_columns(self):
        pass
