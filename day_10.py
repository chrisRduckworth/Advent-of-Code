def increment_position(pipe, direction):
    """returns an increment for the coords"""
    if pipe not in "|-LJ7F":
        raise ValueError("input must be pipe")
    if pipe == "|":
        if direction not in "NS":
            raise ValueError("invalid direction")
        return (0, 1) if direction == "N" else (0, -1)
    if pipe == "-":
        if direction not in "EW":
            raise ValueError("invalid direction")
        return (1, 0) if direction == "W" else (-1,0)
    if pipe == "L":
        if direction not in "NE":
            raise ValueError("invalid direction")
        return (1, 0) if direction == "N" else (0, -1)
    if pipe == "J":
        if direction not in "NW":
            raise ValueError("invalid direction")
        return (-1, 0) if direction == "N" else (0, -1)
    if pipe == "7":
        if direction not in "SW":
            raise ValueError("invalid direction")
        return (0, 1) if direction == "W" else (-1, 0)
    if pipe == "F":
        if direction not in "SE":
            raise ValueError("invalid direction")
        return (0, 1) if direction == "E" else (1, 0)

def find_start_coordinates(maze):
    """finds starting coordinates of the maze"""
    for i, row in enumerate(maze):
        if "S" in row:
            return (row.find("S"), i)

def furthest_point(maze):
    maze = maze.splitlines()
    start_position = find_start_coordinates(maze)
    pass

