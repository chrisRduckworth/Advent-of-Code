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
    movement_directions = {(0,1): "N", (0, -1): "S", (1, 0): "W", (-1, 0): "E"}
    # for my input start connects to south and west. We choose south
    movement = (0, 1)
    route = [start_position, (start_position[0], start_position[1] + 1)]
    while maze[route[-1][1]][route[-1][0]] != "S":
        movement = increment_position(maze[route[-1][1]][route[-1][0]], movement_directions[movement])
        route.append((route[-1][0] + movement[0], route[-1][1] + movement[1]))
    return len(route[:-1]) / 2

if __name__ == "__main__":
    with open("inputs/day_10.txt") as f:
        maze = f.read()
        distance_to_furthest_point = furthest_point(maze)
        print(distance_to_furthest_point, "< distance to furthest point")
