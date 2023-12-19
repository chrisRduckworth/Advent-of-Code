from day_19 import get_info, eval_rule, eval_part, sum_accepted, find_new_range

class TestGetInfo:
    def test_returns_parts(self):
        system = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
        
        expected = [{"x":787, "m":2655, "a":1222, "s":2876},
                    {"x":1679, "m":44, "a":2067, "s":496},
                    {"x":2036, "m":264, "a":79, "s":2244},
                    {"x":2461, "m":1339, "a":466, "s":291},
                    {"x":2127, "m":1623, "a":2188, "s":1013}]

        parts = get_info(system)[1]

        assert parts == expected

    def test_returns_rules(self):
        system = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

        expected = {"px":[("a<2006", "qkq"), ("m>2090", "A"), "rfg"],
                    "pv":[("a>1716", "R"), "A"],
                    "lnx":[("m>1548", "A"), "A"],
                    "rfg": [("s<537", "gd"), ("x>2440", "R"), "A"],
                    "qs": [("s>3448", "A"), "lnx"],
                    "qkq":[("x<1416", "A"), "crn"],
                    "crn": [("x>2662", "A"), "R"],
                    "in": [("s<1351", "px"), "qqz"],
                    "qqz": [("s>2770", "qs"), ("m<1801", "hdj"), "R"],
                    "gd": [("a>3333", "R"), "R"],
                    "hdj": [("m>838", "A"), "pv"]
                    }

        rules = get_info(system)[0]

        assert rules == expected

class TestEvalRule:
    def test_returns_output_of_single_rule(self):
        rule = [("s<1351", "px"), "qqz"]

        part = {"x":787, "m":2655, "a":1222, "s":2876}
        part_2 = {"x":1679, "m":44, "a":2067, "s":496}

        assert eval_rule(part, rule) == "qqz"
        assert eval_rule(part_2, rule) == "px"
        
        rule = [("s>2770", "qs"), ("m<1801", "hdj"), "R"]

        part_3 = {"x":1, "m": 2000, "a":1, "s":1}

        assert eval_rule(part, rule) == "qs"
        assert eval_rule(part_2, rule) == "hdj"
        assert eval_rule(part_3, rule) == "R"

class TestEvalPart:
    def test_returns_output_of_part_through_rules(self):
        system = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
        
        rules, parts = get_info(system)

        assert eval_part(parts[0], rules) == "A"
        assert eval_part(parts[1], rules) == "R"
        assert eval_part(parts[2], rules) == "A"
        assert eval_part(parts[3], rules) == "R"
        assert eval_part(parts[4], rules) == "A"
        
class TestSumAccepted:
    def test_returns_sum_of_accepted_parts(self):
        system = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
        
        rules, parts = get_info(system)

        total = sum_accepted(parts, rules)

        assert total == 19114

class TestFindNewRange:
    def test_does_not_modify_original_range(self):
        old_range = {"x":[1,4000], "m":[1,4000], "a":[1,4000], "s":[1,4000]}
        constraint = "a<2006"

        find_new_range(old_range, constraint)

        assert old_range == {"x":[1,4000], "m":[1,4000], "a":[1,4000], "s":[1,4000]}
        
    def test_returns_new_range_if_rule_does_not_overlap(self):
        old_range = {"x":[1,4000], "m":[1,4000], "a":[1,4000], "s":[1,4000]}
        constraint = "a<2006"

        new_range = find_new_range(old_range, constraint)[0]

        assert new_range == {"x":[1,4000], "m":[1,4000], "a":[1,2005], "s":[1,4000]}

        constraint = "x>3000"

        new_range = find_new_range(new_range, constraint)[0]

        assert new_range == {"x":[3001,4000], "m":[1,4000], "a":[1,2005], "s":[1,4000]}

    def test_returns_leftover_range_for_pass_through(self):
        old_range = {"x":[1,4000], "m":[1,4000], "a":[1,4000], "s":[1,4000]}
        constraint = "a<2006"

        pass_through = find_new_range(old_range, constraint)[1]

        assert pass_through == {"x":[1,4000], "m":[1,4000], "a":[2006,4000], "s":[1,4000]}

        constraint = "x>3000"

        pass_through = find_new_range(pass_through, constraint)[1]

        assert pass_through == {"x":[1,3000], "m":[1,4000], "a":[2006, 4000], "s":[1,4000]}

    def test_works_when_constraint_overlaps(self):
        old_range = {"x":[1,3000], "m":[1,4000], "a":[2006, 4000], "s":[1,4000]}
        constraint = "a>3000"

        new_range,pass_through = find_new_range(old_range, constraint)

        assert new_range == {"x":[1,3000], "m":[1,4000], "a":[3001, 4000], "s":[1,4000]}
        assert pass_through == {"x":[1,3000], "m":[1,4000], "a":[2006, 3000], "s":[1,4000]}

        old_range = {"x":[3001,4000], "m":[1,4000], "a":[1,2005], "s":[1,4000]} 
        constraint = "a<1500"

        new_range,pass_through = find_new_range(old_range, constraint)

        assert new_range == {"x":[3001,4000], "m":[1,4000], "a":[1,1499], "s":[1,4000]}
        assert pass_through == {"x":[3001,4000], "m":[1,4000], "a":[1500, 2005], "s":[1,4000]}

    def test_returns_0_if_constrain_out_of_bounds(self):
        old_range = {"x":[3001,4000], "m":[1,4000], "a":[1,2005], "s":[1,4000]}
        constraint = "x>2500"

        new_range,pass_through = find_new_range(old_range, constraint)

        assert new_range == {"x":[3001,4000], "m":[1,4000], "a":[1,2005], "s":[1,4000]}
        assert pass_through == 0

        constraint = "a<3000"
        
        new_range,pass_through = find_new_range(old_range, constraint)
        
        assert new_range == {"x":[3001,4000], "m":[1,4000], "a":[1,2005], "s":[1,4000]}
        assert pass_through == 0

        constraint = "x<2500"
        
        new_range,pass_through = find_new_range(old_range, constraint)
        
        assert new_range == 0
        assert pass_through == {"x":[3001,4000], "m":[1,4000], "a":[1,2005], "s":[1,4000]}

        constraint = "a>3000"
        
        new_range,pass_through = find_new_range(old_range, constraint)
        
        assert new_range == 0
        assert pass_through == {"x":[3001,4000], "m":[1,4000], "a":[1,2005], "s":[1,4000]}
