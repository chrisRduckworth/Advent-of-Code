from day_10 import increment_position
import pytest

class TestIncrementPosition:
    def test_returns_tuple_of_increment(self):
        assert increment_position("|", "N") == (0, 1)
        assert increment_position("|", "S") == (0, -1)
        
        assert increment_position("-", "W") == (1, 0)
        assert increment_position("-", "E") == (-1, 0)
        
        assert increment_position("L", "N") == (1, 0)
        assert increment_position("L", "E") == (0, -1)

        assert increment_position("J", "N") == (-1, 0)
        assert increment_position("J", "W") == (0, -1)

        assert increment_position("7", "W") == (0, 1)
        assert increment_position("7", "S") == (-1, 0)

        assert increment_position("F", "E") == (0, 1)
        assert increment_position("F", "S") == (1, 0)

    def test_raises_error_if_given_ground(self):
        with pytest.raises(ValueError) as exc_info:
            increment_position(".", "S")
        assert exc_info.type is ValueError
        assert exc_info.value.args[0] == "input must be pipe"
