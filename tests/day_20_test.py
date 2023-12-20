from day_20 import Module, Button, Broadcaster, FlipFlop, Conjunction


class TestModule:
    def test_inits_correctly(self):
        m = Module("a", ["b"])

        assert m.name == "a"
        assert m.sent_high == 0
        assert m.sent_low == 0
        assert m.to_send == 0
        assert m.connections == ["b"]

    def test_send_pulse_appends(self):
        m_a = Module("a", ["b"])
        m_b = Module("b", ["a"])
        m_a.to_send = "low"
        queue = []

        m_a.send_pulse(queue)

        assert queue == [["b", "a", "low"]]

        m_b.to_send = "high"

        m_b.send_pulse(queue)

        assert queue == [["b", "a", "low"], ["a", "b", "high"]]

    def test_send_pulse_appends_all_connections(self):
        m_a = Module("a", ["b", "c", "d"])
        m_a.to_send = "low"
        queue = []

        m_a.send_pulse(queue)

        assert queue == [["b", "a", "low"], [
            "c", "a", "low"], ["d", "a", "low"]]

    def test_get_sent_high(self):
        m_a = Module("a", ["b", "c", "d"])
        m_a.to_send = "high"
        queue = []

        m_a.send_pulse(queue)

        assert m_a.get_sent_high() == 3

    def test_get_sent_low(self):
        m_a = Module("a", ["b", "c", "d", "e"])
        m_a.to_send = "low"
        queue = []

        m_a.send_pulse(queue)

        assert m_a.get_sent_low() == 4


class TestButton:
    def test_inits_correctly(self):
        button = Button("a", ["b"])

        assert button.name == "a"
        assert button.sent_high == 0
        assert button.sent_low == 0
        assert button.to_send == "low"
        assert button.connections == ["b"]


class TestBroadcaster():
    def test_inits_correctly(self):
        broadcaster = Broadcaster("broadcaster", ["a", "b", "c"])

        assert broadcaster.name == "broadcaster"
        assert broadcaster.sent_high == 0
        assert broadcaster.sent_low == 0
        assert broadcaster.to_send == 0
        assert broadcaster.connections == ["a", "b", "c"]

    def test_handle_pulse_takes_input_to_send(self):
        broadcaster = Broadcaster("broadcaster", ["a", "b", "c"])

        broadcaster.handle_pulse("low", [])

        assert broadcaster.to_send == "low"

        broadcaster.handle_pulse("high", [])

        assert broadcaster.to_send == "high"

    def test_handl_pulse_appends(self):
        broadcaster = Broadcaster("broadcaster", ["a", "b", "c"])
        queue = []

        broadcaster.handle_pulse("low", queue)

        assert queue == [["a", "broadcaster", "low"], [
            "b", "broadcaster", "low"], ["c", "broadcaster", "low"]]

        broadcaster.handle_pulse("high", queue)

        assert queue == [["a", "broadcaster", "low"], ["b", "broadcaster", "low"], ["c", "broadcaster", "low"], [
            "a", "broadcaster", "high"], ["b", "broadcaster", "high"], ["c", "broadcaster", "high"]]


class TestFlipFlop:
    def test_inits_corrrectly(self):
        flip_flop = FlipFlop("a", ["b", "c"])

        assert flip_flop.name == "a"
        assert flip_flop.sent_high == 0
        assert flip_flop.sent_low == 0
        assert flip_flop.to_send == 0
        assert flip_flop.connections == ["b", "c"]
        assert flip_flop.switch == "off"

    def test_handle_pulse_sending_high(self):
        flip_flop = FlipFlop("a", ["b", "c"])
        queue = []

        flip_flop.handle_pulse("high", queue)

        assert flip_flop.switch == "off"
        assert flip_flop.to_send == 0
        assert queue == []

        flip_flop.switch = "on"

        flip_flop.handle_pulse("high", queue)

        assert flip_flop.switch == "on"
        assert flip_flop.to_send == 0
        assert queue == []

    def test_handle_pulse_sending_low_switches_switch(self):
        flip_flop = FlipFlop("a", ["b", "c"])

        flip_flop.handle_pulse("low", [])

        assert flip_flop.switch == "on"

        flip_flop.handle_pulse("low", [])

        assert flip_flop.switch == "off"

    def test_appends_correct_val_when_sending(self):
        flip_flop = FlipFlop("a", ["b", "c"])
        queue = []

        flip_flop.handle_pulse("low", queue)

        assert queue == [["b", "a", "high"], ["c", "a", "high"]]

        flip_flop.handle_pulse("low", queue)

        assert queue == [["b", "a", "high"], ["c", "a", "high"], [
            "b", "a", "low"], ["c", "a", "low"]]


class TestConjunction:
    def test_inits_correctly(self):
        conjunction = Conjunction("a", ["b", "c"], ["d", "e", "f"])

        assert conjunction.name == "a"
        assert conjunction.sent_high == 0
        assert conjunction.sent_low == 0
        assert conjunction.to_send == 0
        assert conjunction.connections == ["b", "c"]

        assert conjunction.inputs == {"d": "low", "e": "low", "f": "low"}

    def test_changes_input_value(self):
        conjunction = Conjunction("a", ["b", "c"], ["d", "e", "f"])

        conjunction.handle_pulse("high", [], "d")

        assert conjunction.inputs["d"] == "high"

        conjunction.handle_pulse("low", [], "d")

        assert conjunction.inputs["d"] == "low"

    def test_sends_low_if_all_inputs_high(self):
        conjunction = Conjunction("a", ["b", "c"], ["d", "e", "f"])
        conjunction.inputs = {"d": "high", "e": "high", "f": "low"}
        queue = []

        conjunction.handle_pulse("high", queue, "f")

        assert queue == [["b", "a", "low"], ["c", "a", "low"]]

    def test_sends_high_otherwise(self):
        conjunction = Conjunction("a", ["b", "c"], ["d", "e", "f"])
        queue = []

        conjunction.handle_pulse("high", queue, "d")

        assert queue == [["b", "a", "high"], ["c", "a", "high"]]

        conjunction.handle_pulse("high", queue, "e")

        assert queue == [["b", "a", "high"], ["c", "a", "high"]] * 2
        conjunction.handle_pulse("low", queue, "d")

        assert queue == [["b", "a", "high"], ["c", "a", "high"]] * 3
