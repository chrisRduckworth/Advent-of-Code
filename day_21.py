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

def find_steps(garden, start, starting_step=0):
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

    queue.append((x, y, starting_step))

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

def find_all_endings(garden, s):
    # Note that the garden is a square of odd length,
    # S is in the center of the tile,
    # and that the axes out from S are all empty
    
    # s = steps, w = width of tile
    w = len(garden)
    # l = length of middle row of full tiles
    l = int((2 * (s - w) + 1) / w)

    total = 0

    """Full tiles"""
    # total number of full even tiles 
    E = int(((l + 1) ** 2) / 4)
    # total number of full odd tiles
    O = int(((l - 1) ** 2) / 4)
    
    center = int((w - 1) / 2)
    distances = find_steps(garden, (center, center))
    # number of endings an even number of steps away
    e = find_endings(distances, True)
    # number of endings an odd number of steps away
    o = find_endings(distances, False)

    total += E * e + O * o

    """Axis ends"""
    # tiles at the end of axes are odd
    # and distance is such that it is precisely equal to width
    for x in [(w - 1, center), (center, w - 1), (0, center), (center, 0)]:
        distances = find_steps(garden, x, 1)
        valid_endings = find_endings(distances, False, w)
        total += valid_endings

    """Inner diagonals"""
    # inner diagonals are odd
    # there are (l-1)/2 inner diagonals starting from each corner
    # and all tiles within w + (w-1) / 2 are reachable
    for x in [(0, 0), (0, w-1), (w-1, 0), (w-1, w-1)]:
        distances = find_steps(garden, x)
        valid_endings = find_endings(distances, False, w + (w - 1) / 2 - 1)
        total += valid_endings * int((l - 1) / 2)

    """Outer diagonals"""
    # outer diagonals are even
    # there are (l+1)/2 outer diagonals starting from each corner
    # and all tiles within (w-1)/2 are reachable
    for x in [(0, 0), (0, w-1), (w-1, 0), (w-1, w-1)]:
        distances = find_steps(garden, x)
        valid_endings = find_endings(distances, True, (w - 1) / 2 - 1)
        total += valid_endings * int((l + 1) / 2)
        
    return total

def brute_force(garden, s):
    garden = deepcopy(garden)

    s_y = [i for i, r in enumerate(garden) if "S" in r][0]
    s_x = [i for i, c in enumerate(garden[s_y]) if "S" == c][0]

    garden = [["#" if x == "#" else {} for x in r] for r in garden]
    width = len(garden[0])
    height = len(garden)
    
    queue = []

    def bfs(node):
        x, y, current_steps, tile_pos = node
        if garden[y][x] == "#" or current_steps > s:
            return
        if tile_pos in garden[y][x] and garden[y][x][tile_pos] <= current_steps:
            return

        garden[y][x][tile_pos] = current_steps
        

        x_next = x + 1
        x_prev = x - 1
        tile_x_next = tile_pos[0]
        tile_x_prev = tile_pos[0]

        if x == 0:
            x_prev = width - 1
            tile_x_prev = tile_pos[0] - 1
        elif x == width - 1:
            x_next = 0
            tile_x_next = tile_pos[0] + 1

        y_next = y + 1
        y_prev = y - 1
        tile_y_next = tile_pos[1]
        tile_y_prev = tile_pos[1]

        if y == 0:
            y_prev = height - 1
            tile_y_prev = tile_pos[1] - 1
        elif y == height - 1:
            y_next = 0
            tile_y_next = tile_pos[1] + 1

        queue.append((x_next, y, current_steps + 1, (tile_x_next, tile_pos[1])))
        queue.append((x_prev, y, current_steps + 1, (tile_x_prev, tile_pos[1])))
        queue.append((x, y_next, current_steps + 1, (tile_pos[0], tile_y_next)))
        queue.append((x, y_prev, current_steps + 1, (tile_pos[0], tile_y_prev)))
        
    queue.append((s_x, s_y, 0, (0,0)))

    while queue:
        node = queue.pop(0)
        bfs(node)

    total = 0
    for r in garden:
        for x in r:
            if x != "#":
                for k in x:
                    if x[k] % 2 == s % 2:
                        total += 1

    return total

if __name__ == "__main__":
    with open("inputs/day_21.txt") as f:
        garden = f.read().splitlines()
        garden = [list(r) for r in garden]
        #steps = total_steps(garden, 64)
        #print(steps, "< total steps")
        total_endings = find_all_endings(garden, 26501365)
        print(total_endings, "< total endings")
