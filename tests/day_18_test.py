from day_18 import dig_trench

class TestDigTrench:
    def test_returns_digs_single_instruction(self):
        instructions = [["R", 6, "(#70c710)"]]

        trenches = dig_trench(instructions)

        assert trenches == [["#","#","#","#","#","#","#"]]

        instructions = [["D", 5, "(#0dc571)"]]

        trenches = dig_trench(instructions)

        assert trenches == [["#"],["#"],["#"],["#"],["#"],["#"]]

        instructions = [["L", 2, "(#5713f0)"]]
        
        trenches = dig_trench(instructions)

        assert trenches == [["#","#","#"]]

        instructions = [["U", 3, "(#a77fa3)"]]
        
        trenches = dig_trench(instructions)

        assert trenches == [["#"],["#"],["#"],["#"],]
