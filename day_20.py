import re

class Module:
    def __init__(self, name, connections):
        self.name = name
        self.sent_high = 0
        self.sent_low = 0
        self.to_send = 0
        self.connections = connections

    def send_pulse(self, queue):
        for connection in self.connections:
            # format is [receiver, sender, signal]
            # need sender because of conjunctions >.>
            queue.append([connection, self.name, self.to_send])
            if self.to_send == "low":
                self.sent_low += 1
            else:
                self.sent_high += 1

    def get_sent_high(self):
        return self.sent_high

    def get_sent_low(self):
        return self.sent_low


class Button(Module):
    def __init__(self, name, connections):
        super().__init__(name, connections)
        self.to_send = "low"


class Broadcaster(Module):
    def __init__(self, name, connections):
        super().__init__(name, connections)

    def handle_pulse(self, pulse, queue, input_module=0):
        self.to_send = pulse
        self.send_pulse(queue)


class FlipFlop(Module):
    def __init__(self, name, connections):
        super().__init__(name, connections)
        self.switch = "off"

    def handle_pulse(self, pulse, queue, input_module=0):
        if pulse == "low":
            if self.switch == "on":
                self.switch = "off"
                self.to_send = "low"
            else:
                self.switch = "on"
                self.to_send = "high"

            self.send_pulse(queue)


class Conjunction(Module):
    def __init__(self, name, connections, inputs):
        super().__init__(name, connections)
        self.inputs = {i: "low" for i in inputs}

    def handle_pulse(self, pulse, queue, input_module):
        self.inputs[input_module] = pulse
        if all(v == "high" for v in self.inputs.values()):
            self.to_send = "low"
            self.send_pulse(queue)
        else:
            self.to_send = "high"
            self.send_pulse(queue)
        pass


def create_modules(in_string):
    in_string = in_string.splitlines()
    in_string = [r.replace(" ", "").split("->") for r in in_string]
    in_string = [[r[0], r[1].split(",")] for r in in_string]

    modules = {}
    modules["button"] = Button("name", ["broadcaster"])
    
    for r in in_string:
        name, connections = r
        if name == "broadcaster":
            modules["broadcaster"] = Broadcaster("broadcaster", connections)
        elif name[0] == "%":
            modules[name[1:]] = FlipFlop(name[1:], connections)
        elif name[0] == "&":
            inputs = []
            for m in in_string:
                if name[1:] in m[1]:
                    inputs.append(m[0].replace("%", "").replace("&", ""))
            modules[name[1:]] = Conjunction(name[1:], connections, {i: "low" for i in inputs})
    return modules
