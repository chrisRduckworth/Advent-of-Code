from copy import deepcopy

def total_steps(garden, steps):
    garden.insert(0, list("#" * len(garden[0])))
    garden.append(list("#" * len(garden[0])))
    garden = [["#", *r, "#"] for r in garden]
    
    s_y = [i for i, r in enumerate(garden) if "S" in r][0]
    s_x = [i for i, c in enumerate(garden[s_y]) if "S" == c][0]

    def flood_fill(x, y, current_steps):
        if garden[y][x] == "#" or current_steps > steps:
            return
        if isinstance(garden[y][x], int):
            if garden[y][x] <= current_steps:
                return
        garden[y][x] = current_steps
        flood_fill(x + 1, y, current_steps + 1)
        flood_fill(x - 1, y, current_steps + 1)
        flood_fill(x, y + 1, current_steps + 1)
        flood_fill(x, y - 1, current_steps + 1)
        return 
        
    flood_fill(s_x, s_y, 0)

    total = 0 
    for j, y in enumerate(garden):
        for i, x in enumerate(y):
            if isinstance(x, int):
                if x % 2 == steps % 2:
                    total += 1
    return total

def find_steps(garden, start):
    """returns an array of the distances from a start point"""
    # pad garden with #s
    garden = deepcopy(garden)
    garden.insert(0, list("#" * len(garden[0])))
    garden.append(list("#" * len(garden[0])))
    garden = [["#", *r, "#"] for r in garden]

    x = start[0] + 1
    y = start[1] + 1

    queue = []
    
    def bfs(node):
        x, y, current_steps = node
        if garden[y][x] == "#":
            return
        if isinstance(garden[y][x], int):
            if garden[y][x] <= current_steps:
                return

        garden[y][x] = current_steps
        queue.append((x + 1, y, current_steps + 1))
        queue.append((x - 1, y, current_steps + 1))
        queue.append((x, y + 1, current_steps + 1))
        queue.append((x, y - 1, current_steps + 1))

    queue.append((x, y, 0))

    while queue:
        node = queue.pop(0)
        bfs(node)

    return [r[1:-1] for r in garden[1:-1]]

def find_endings(distances, even, within=-1):
    """returns number of valid endings within set distance"""
    remainder = 0 if even else 1

    total = 0
    for y in distances:
        for x in y:
            if isinstance(x, int) and x % 2 == remainder:
                if within == -1 or x <= within:
                    total += 1

    return total

if __name__ == "__main__":
    with open("inputs/day_21.txt") as f:
        garden = f.read().splitlines()
        garden = [list(r) for r in garden]
        steps = total_steps(garden, 64)
        print(steps, "< total steps")
