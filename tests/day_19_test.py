from day_19 import get_info, eval_rule

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
