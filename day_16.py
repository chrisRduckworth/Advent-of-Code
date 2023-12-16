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

"""
def find_energized_tiles(pattern, position, direction, running_total, visited):
    if [position, direction] in visited or is_moving_to_edge(position, direction, (len(pattern[0]), len(pattern))):
        print(position, direction, running_total, "terminating")
        print(visited)
        print(len(visited))
        print({str(v[0]) for v in visited})
        print(len({str(v[0]) for v in visited}))
        return running_total
    
    x, y = position
    visited.append([(x,y), direction])
    
    if direction == "N": y -= 1
    if direction == "S": y += 1
    if direction == "E": x += 1
    if direction == "W": x -= 1

    if pattern[y][x] == ".":
        return find_energized_tiles(pattern, (x,y), direction, running_total + 1, visited)
    
    if pattern[y][x] == "\\":
        if direction == "N": direction = "W"
        elif direction == "E": direction = "S"
        elif direction == "S": direcion = "E"
        else: direction = "N"
        return find_energized_tiles(pattern, (x,y), direction, running_total + 1, visited)

    if pattern[y][x] == "/":
        if direction == "N": direction = "E"
        elif direction == "E": direction = "N"
        elif direction == "S": direcion = "W"
        else: direction = "S"
        return find_energized_tiles(pattern, (x,y), direction, running_total + 1, visited)

    if pattern[y][x] == "|":
        if direction in "NS":
            return find_energized_tiles(pattern, (x,y), direction, running_total + 1, visited)

        return find_energized_tiles(pattern, (x,y), "N", running_total + 1, visited) + find_energized_tiles(pattern, (x,y), "S", 0, visited)

    if pattern[y][x] == "-":
        if direction in "EW":
            return find_energized_tiles(pattern, (x,y), direction, running_total + 1, visited)
        
        return find_energized_tiles(pattern, (x,y), "E", running_total + 1, visited) + find_energized_tiles(pattern, (x,y), "W", 0, visited)
    pass
"""

def find_energized_tiles(pattern):
    visited = []
    def find_next_position(position, direction):
        print(position, direction)
        nonlocal pattern
        nonlocal visited
        if (position, direction) in visited:
            return

        if is_moving_to_edge(position, direction, (len(pattern[0]), len(pattern))):
            visited.append((position, direction))
            return
        
        x,y = position
        visited.append((position, direction))
        
        position_lookup = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
        x += position_lookup[direction][0]
        y += position_lookup[direction][1]
        
        if pattern[y][x] == ".":
            find_next_position((x,y), direction)

        elif pattern[y][x] == "/":
            direction_lookup = {"N": "E", "E": "N", "S": "W", "W": "S"}
            find_next_position((x,y), direction_lookup[direction])

        elif pattern[y][x] == "\\":
            direction_lookup = {"N": "W", "E": "S", "S": "E", "W": "N"}
            find_next_position((x,y), direction_lookup[direction])

        elif pattern[y][x] == "-":
            if direction in "EW":
                find_next_position((x,y), direction)
            else:
                find_next_position((x,y), "E")
                find_next_position((x,y), "W")

        elif pattern[y][x] == "|":
            if direction in "NS":
                find_next_position((x,y), direction)
            else:
                find_next_position((x,y), "N")
                find_next_position((x,y), "S")
        
    find_next_position((-1,0), "E")
    return len(set(str(v[0]) for v in visited)) - 1
