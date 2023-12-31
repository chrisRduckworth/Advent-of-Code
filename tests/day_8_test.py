from day_8 import find_steps, find_ghost_steps

class TestFindSteps:
    def test_returns_1_for_simple_case(self):
        maps = "L\n\nAAA = (ZZZ, AAA)\nZZZ = (ZZZ, ZZZ)"

        steps = find_steps(maps)

        assert steps == 1

    def test_returns_steps_for_long_directions(self):
        maps = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

        steps = find_steps(maps)

        assert steps == 2

    def test_returns_steps_for_short_directions(self):
        maps = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

        steps = find_steps(maps)

        assert steps == 6
        
class TestFindGhostSteps:
    def test_returns_1_for_simple_case(self):
        maps = "L\n\nAAA = (ZZZ, AAA)\nZZZ = (ZZZ, ZZZ)"

        steps = find_ghost_steps(maps)

        assert steps == 1
    
    def test_returns_steps_for_long_directions(self):
        maps =   """LRLRLRLRLR

AAA = (AAB, XXX)
AAB = (XXX, AAZ)
AAZ = (AAB, XXX)
BBA = (BBB, XXX)
BBB = (BBC, BBC)
BBC = (BBZ, BBZ)
BBZ = (BBB, BBB)
XXX = (XXX, XXX)"""  
        
        steps = find_ghost_steps(maps)

        assert steps == 6
    
    def test_returns_steps_for_short_directions(self):
        maps =   """LR

AAA = (AAB, XXX)
AAB = (XXX, AAZ)
AAZ = (AAB, XXX)
BBA = (BBB, XXX)
BBB = (BBC, BBC)
BBC = (BBZ, BBZ)
BBZ = (BBB, BBB)
XXX = (XXX, XXX)"""  
        
        steps = find_ghost_steps(maps)

        assert steps == 6
