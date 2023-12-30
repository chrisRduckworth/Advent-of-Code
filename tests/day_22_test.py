from day_22 import create_tower, blocks_below

class TestCreateTower:
    def test_turns_single_block_into_tower(self):
        blocks = [((2,0,0), (2,2,0))]

        tower = create_tower(blocks)

        assert tower == [[[False, False, 1], [False, False, 1], [False, False, 1]]]

    def test_includes_3_dimensions(self):
        blocks = [((1,1,0), (1,1,2))]

        tower = create_tower(blocks)

        assert tower == [[[False, False], [False, 1]],[[False, False], [False, 1]],[[False, False], [False, 1]]]
    
    def test_has_correct_lengths(self):
        blocks = [((1,1,0), (1,1,2)), ((2,0,1), (2,2,1)), ((0,1,3), (3,1,3))]

        tower = create_tower(blocks)

        assert len(tower) == 4
        assert len(tower[0]) == 3
        assert len(tower[0][0]) == 4

    def test_creates_blocks_length_1(self):
        blocks = [((1,1,1), (1,1,1))]

        tower = create_tower(blocks)

        assert tower == [[[False, False], [False, False]], [[False, False], [False, 1]]]

    def test_creates_multiple_blocks(self):
        blocks =[
                ((1,0,1), (1,2,1)),
                ((0,0,2), (2,0,2)),
                ((0,2,3), (2,2,3)),
                ((0,0,4), (0,2,4)),
                ((2,0,5), (2,2,5)),
                ((0,1,6), (2,1,6)),
                ((1,1,8), (1,1,9)),
                ((2,2,10), (2,2,10)),
                ]

        expected = [
                [[False, False, False],
                 [False, False, False],
                 [False, False, False],],
                [[False, 1, False],
                 [False, 1, False],
                 [False, 1, False],],
                [[2, 2, 2],
                 [False, False, False],
                 [False, False, False],],
                [[False, False, False],
                 [False, False, False],
                 [3, 3, 3],],
                [[4, False, False],
                 [4, False, False],
                 [4, False, False],],
                [[False, False, 5],
                 [False, False, 5],
                 [False, False, 5],],
                [[False, False, False],
                 [6, 6, 6],
                 [False, False, False],],
                [[False, False, False],
                 [False, False, False],
                 [False, False, False],],
                [[False, False, False],
                 [False, 7, False],
                 [False, False, False],],
                [[False, False, False],
                 [False, 7, False],
                 [False, False, False],],
                [[False, False, False],
                 [False, False, False],
                 [False, False, 8],],
                ]

        tower = create_tower(blocks)

        assert tower == expected


class TestBlocksBelow:
    def test_returns_empty_if_no_blocks_below(self):
        tower = create_tower([((1,1,1), (1,1,1))])

        below = blocks_below(tower, 1)

        assert below == set()

    def test_returns_empty_if_on_bottom_row(self):
        tower = create_tower([((1,1,0), (1,1,0))])

        below = blocks_below(tower, 1)

        assert below == set()

    def test_returns_single_block_below(self):
        tower = create_tower([
            ((1,1,1), (1,1,1)),
            ((1,1,0), (1,1,0))
            ])

        below = blocks_below(tower, 1)

        assert below == {2}

    def test_does_not_include_itself(self):
        tower = create_tower([
            ((1,1,1), (1,1,4))
            ])
        
        below = blocks_below(tower, 1)

        assert below == set()

    def test_returns_multiple_below(self):
        tower = create_tower([
            ((0,0,0), (0,0,0)),
            ((1,0,0), (1,0,0)),
            ((0,0,1), (1,0,1))
            ])

        below = blocks_below(tower, 3)

        assert below == {1, 2}
