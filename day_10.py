import re

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

def find_route(maze, initial_movement):
    start_position = find_start_coordinates(maze)
    movement_directions = {(0,1): "N", (0, -1): "S", (1, 0): "W", (-1, 0): "E"}
    route = [start_position, (start_position[0] + initial_movement[0], start_position[1] + initial_movement[1])]
    movement = initial_movement
    while maze[route[-1][1]][route[-1][0]] != "S":
        movement = increment_position(maze[route[-1][1]][route[-1][0]], movement_directions[movement])
        route.append((route[-1][0] + movement[0], route[-1][1] + movement[1]))
    return route[:-1]

def furthest_point(maze, initial_movement):
    maze = maze.splitlines()
    route = find_route(maze, initial_movement)
    return len(route) / 2

def mark_adjacent_tiles(maze, position, facing):
    """marks adjacent tiles I or O if they're inside/outside"""
    # pad maze for when the position is at the edge
    x, y = (position[0] + 1, position[1] + 1)
    padded_maze = ["." * (len(maze[0]) + 2), *[f".{row}." for row in maze], "." * (len(maze[0]) + 2)]
    if facing == "N":
        if padded_maze[y][x-1] not in "FJ7L|-S":
            padded_maze[y] = padded_maze[y][:x-1] + "I" + padded_maze[y][x:]
        if padded_maze[y][x+1] not in "FJ7L|-S":
            padded_maze[y] = padded_maze[y][:x+1] + "O" + padded_maze[y][x+2:]
    elif facing == "E":
        if padded_maze[y-1][x] not in "FJ7L|-S":
            padded_maze[y-1] = padded_maze[y-1][:x] + "I" + padded_maze[y-1][x+1:]
        if padded_maze[y+1][x] not in "FJ7L|-S":
            padded_maze[y+1] = padded_maze[y+1][:x] + "O" + padded_maze[y+1][x+1:]
    elif facing == "S":
        if padded_maze[y][x-1] not in "FJ7L|-S":
            padded_maze[y] = padded_maze[y][:x-1] + "O" + padded_maze[y][x:]
        if padded_maze[y][x+1] not in "FJ7L|-S":
            padded_maze[y] = padded_maze[y][:x+1] + "I" + padded_maze[y][x+2:]
    elif facing == "W":
        if padded_maze[y-1][x] not in "FJ7L|-S":
            padded_maze[y-1] = padded_maze[y-1][:x] + "O" + padded_maze[y-1][x+1:]
        if padded_maze[y+1][x] not in "FJ7L|-S":
            padded_maze[y+1] = padded_maze[y+1][:x] + "I" + padded_maze[y+1][x+1:]
    return [row[1:-1] for row in padded_maze[1:-1]]

def enclosed_tiles(maze, initial_movement):
    maze = maze.splitlines()
    route = find_route(maze, initial_movement)
    maze = ["".join(char if (x,y) in route else "." for x, char in enumerate(row))for y, row in enumerate(maze)]
    # starting position will be first point on top row in the route
    # this must be "F"
    # by turning "left" and travelling anticlockwise, everything on the right
    # of our route will be outside, and everything on the left will be inside
    for y, row in enumerate(maze):
        if row != "." * len(maze[0]):
            for x, char in enumerate(row):
                if char != ".":
                    start_position = (x, y)
                    break
            break
    
    start_index = route.index(start_position)
    facing = "W"
    
    # check if we're moving anticlockwise or clockwise:
    if (start_position[1] - route[start_index + 1][1]) == 0:
        # we are moving clockwise, so right hand is on the inside
        facing_changes = {(0,1): "N", (0, -1): "S", (1, 0): "W", (-1, 0): "E"}
    else:
        # we are moving anticlockwise, so left hand is inside
        facing_changes = {(0,1): "S", (0, -1): "N", (1, 0): "E", (-1, 0): "W"}
        
    for i in range (start_index, start_index + len(route)):
        index = i % len(route)
        position = route[index]
        maze = mark_adjacent_tiles(maze, position, facing)
        facing_change = (route[(index + 1) % len(route)][0] - position[0], route[(index + 1) % len(route)][1] - position[1])
        facing = facing_changes[facing_change]
        maze = mark_adjacent_tiles(maze, position, facing)
        
    # now we need to fill the gaps with I 
    for i, row in enumerate(maze):
        row = re.sub(r"(?<=I)\.+", lambda m: "I" * len(m[0]), row)
        row = re.sub(r"\.+(?=I)", lambda m: "I" * len(m[0]), row)
        maze[i] = row
    
    return "".join(maze).count("I")


if __name__ == "__main__":
    with open("inputs/day_10.txt") as f:
        maze = f.read()
        # for my input, start connects to south and west. We choose south
        distance_to_furthest_point = furthest_point(maze, (0,1))
        print(distance_to_furthest_point, "< distance to furthest point")
        count_enclosed_tiles = enclosed_tiles(maze, (0,1))
        print(count_enclosed_tiles, "< number of enclosed tiles")
