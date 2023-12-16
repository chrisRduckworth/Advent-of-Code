def is_moving_to_edge(position, direction, dimensions):
    x, y = position
    length, height = dimensions
    if y == 0 and direction == "N":
        return True
    if y == height - 1 and direction == "S":
        return True
    if x == 0 and direction == "W":
        return True
    if x == length - 1 and direction == "E":
        return True
    return False
