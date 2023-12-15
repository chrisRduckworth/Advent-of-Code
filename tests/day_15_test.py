from day_15 import calc_new_value, calc_value, dash, equals, focusing_power

class TestCalcNewValue:
    def test_returns_correct_value_starting_at_zero(self):
        assert calc_new_value(0, "H") == 200

    def test_returns_correct_value(self):
        assert calc_new_value(200, "A") == 153
        assert calc_new_value(153, "S") == 172
        assert calc_new_value(172, "H") == 52

class TestCalcValue:
    def test_calculates_value_for_sequence(self):
        assert calc_value("rn=1") == 30
        assert calc_value("cm-") == 253
        assert calc_value("qp=3") == 97
        assert calc_value("cm=2") == 47
        assert calc_value("qp-") == 14
        assert calc_value("pc=4") == 180
        assert calc_value("ot=9") == 9
        assert calc_value("ab=5") == 197
        assert calc_value("pc-") == 48
        assert calc_value("pc=6") == 214
        assert calc_value("ot=7") == 231

class TestDash:
    def test_does_nothing_if_label_not_present(self):
        labels = {"rn": 1}
        boxes = {0:["rn"]}
        step = "cm-"

        labels, boxes = dash(labels, boxes, step)

        assert labels == {"rn": 1}
        assert boxes == {0: ["rn"]}

    def test_removes_label_from_labels(self):
        labels = {"rn": 1}
        boxes = {0:["rn"]}
        step = "rn-"

        labels, boxes = dash(labels, boxes, step)

        assert labels == {}

    def test_removes_label_from_box(self):
        labels = {"rn": 1}
        boxes = {0:["rn"]}
        step = "rn-"

        labels, boxes = dash(labels, boxes, step)

        assert boxes == {0:[]}

class TestEquals:
    def test_if_label_exists_update_focal_length(self):
        labels = {"rn": 1, "cm": 2, "ot":9, "ab":5, "pc":6}
        boxes = {0:["rn", "cm"], 3:["ot", "ab", "pc"]}
        step = "ot=7"

        labels, boxes = equals(labels, boxes, step)

        assert labels == {"rn": 1, "cm": 2, "ot":7, "ab":5, "pc":6}
        
    def test_does_not_affect_boxes_if_label_exists(self):
        labels = {"rn": 1, "cm": 2, "ot":9, "ab":5, "pc":6}
        boxes = {0:["rn", "cm"], 3:["ot", "ab", "pc"]}
        step = "ot=7"

        labels, boxes = equals(labels, boxes, step)

        assert boxes == {0:["rn", "cm"], 3:["ot", "ab", "pc"]}

    def test_adds_label_to_labels_if_doesnt_exist(self):
        labels = {"rn": 1, "cm": 2, "ot":9, "ab":5, "pc":6}
        boxes = {0:["rn", "cm"], 1:[], 3:["ot", "ab", "pc"]}
        step = "qp=3"

        labels, boxes = equals(labels, boxes, step)

        assert labels == {"rn": 1, "cm": 2, "ot":9, "ab":5, "pc":6, "qp": 3}

    def test_adds_label_to_box(self):
        labels = {"rn": 1, "ot":9, "ab":5, "pc":6}
        boxes = {0:["rn"], 3:["ot", "ab", "pc"]}
        step = "cm=2"

        labels, boxes = equals(labels, boxes, step)

        assert boxes == {0:["rn", "cm"], 3:["ot", "ab", "pc"]}

class TestFocusingPower:
    def test_calculates_focusing_power(self):
        sequence = ["rn=1", "cm-", "qp=3", "cm=2", "qp-", "pc=4", "ot=9", "ab=5", "pc-", "pc=6", "ot=7"]

        assert focusing_power(sequence) == 145
