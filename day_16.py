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

def find_energized_tiles(pattern, i_pos=(-1,0), i_dir="E"):
    visited = []
    def find_next_position(position, direction):
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
            return find_next_position((x,y), direction)

        elif pattern[y][x] == "/":
            direction_lookup = {"N": "E", "E": "N", "S": "W", "W": "S"}
            return find_next_position((x,y), direction_lookup[direction])

        elif pattern[y][x] == "\\":
            direction_lookup = {"N": "W", "E": "S", "S": "E", "W": "N"}
            return find_next_position((x,y), direction_lookup[direction])

        elif pattern[y][x] == "-":
            if direction in "EW":
                return find_next_position((x,y), direction)
            else:
                find_next_position((x,y), "E")
                return find_next_position((x,y), "W")

        elif pattern[y][x] == "|":
            if direction in "NS":
                return find_next_position((x,y), direction)
            else:
                find_next_position((x,y), "N")
                return find_next_position((x,y), "S")
        
    find_next_position(i_pos, i_dir)
    return len(set(str(v[0]) for v in visited)) - 1

def find_optimal_position(pattern):
    values = []
    for y in range(len(pattern)):
        values.append(find_energized_tiles(pattern, (-1, y), "E"))
        values.append(find_energized_tiles(pattern, (len(pattern[0]), y), "W"))

    for x in range(len(pattern[0])):
        values.append(find_energized_tiles(pattern, (x, -1), "S"))
        values.append(find_energized_tiles(pattern, (x, len(pattern)), "N"))
    
    return max(values)

if __name__ == "__main__":
    with open("inputs/day_16.txt") as f:
        pattern = [list(row) for row in f.read().splitlines()]
        energized = find_energized_tiles(pattern)
        print(energized, "< energized")
        optimal = find_optimal_position(pattern)
        print(optimal, "< optimal")
