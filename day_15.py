from functools import reduce

def calc_new_value(current, char):
    current += ord(char)
    current *= 17
    current %= 256
    return current

def calc_value(step):
    """calculates the value of a sequence"""
    total = reduce(calc_new_value, step, 0)
    return total

def dash(labels, boxes, step):
    """removes the lens from labels and boxes"""
    label = step[:-1]
    box_number = calc_value(label)
    if label not in labels:
        return labels, boxes
    
    del labels[label]
    
    i = boxes[box_number].index(label)
    del boxes[box_number][i]
    
    return labels, boxes

def equals(labels, boxes, step):
    """adds or replaces lens"""
    label = step[:-2]
    box_number = calc_value(label)
    focal_length = int(step[-1])
    
    if label not in labels:
        boxes[box_number].append(label)
    labels[label] = focal_length
    
    return labels, boxes

def focusing_power(sequence):
    """calculates the focusing power after executing the sequence"""
    labels = {}
    boxes = {i:[] for i in range(256)}
    for step in sequence:
        if "-" in step:
            labels, boxes = dash(labels, boxes, step)
        else:
            labels, boxes = equals(labels, boxes, step)
    total = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(boxes[box]):
            total += (i + 1) * (j + 1) * labels[lens]
    return total

if __name__ == "__main__":
    with open("inputs/day_15.txt") as f:
        sequence = f.read().split(",")
        total = sum(calc_value(step) for step in sequence)
        print(total, "< total")
