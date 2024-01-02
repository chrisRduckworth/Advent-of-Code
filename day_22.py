from itertools import chain
from copy import deepcopy

def create_tower(blocks):
    """creates a 3d array of blocks"""
    # position (x,y,z) = tower[z][y][x]
    max_x = max(block[1][0] for block in blocks) + 1
    max_y = max(block[1][1] for block in blocks) + 1
    max_z = max(block[1][2] for block in blocks) + 1

    tower = [[[False] * max_x for y in range(max_y)] for z in range(max_z)]
    
    for i, block in enumerate(blocks):
        if block[0][0] != block[1][0]:
            # change is in x
            start_x = block[0][0] 
            end_x = block[1][0] + 1
            y, z = block[0][1:]
            for x in range(start_x, end_x):
                tower[z][y][x] = i + 1
        elif block[0][1] != block[1][1]:
            # change is in y
            start_y = block[0][1]
            end_y = block[1][1] + 1
            x, z = block[1][::2]
            for y in range(start_y, end_y):
                tower[z][y][x] = i + 1
        elif block[0][2] != block[1][2]:
            # change is in z
            start_z = block[0][2]
            end_z = block[1][2] + 1
            x, y = block[0][:2]
            for z in range(start_z, end_z):
                tower[z][y][x] = i + 1
        else:
            # single length block
            x, y, z = block[0]
            tower[z][y][x] = i + 1
            
    return tower

def blocks_below(tower, block, block_number, above=False):
    """returns the blocks above or below the given block"""
    below = set()

    z = block[1][2] if above else block[0][2]
    if z == len(tower) - 1 and above or z == 0 and not above:
        return below

    slice = tower[z]
    for y, r in enumerate(slice):
        for x, b in enumerate(r):
            block_below = tower[z+1][y][x] if above else tower[z-1][y][x]
            if b == block_number and block_below not in [False, b]:
                below.add(block_below)
    
    return below

def fall_blocks(blocks):
    prev_blocks = []
    while prev_blocks != blocks:
        prev_blocks = deepcopy(blocks)
        tower = create_tower(blocks)
        for block, coords in enumerate(blocks):
            if len(blocks_below(tower, coords, block + 1)) == 0 and coords[0][2] != 0:
                coords[0][2] -= 1
                coords[1][2] -= 1

    return blocks

def count_disintegrate(blocks):
    tower = create_tower(blocks)
    total = 0
    for block_number, block in enumerate(blocks):
        # a block b is valid if, for each block above it,
        # there are more than 1 blocks below it - b and atleast
        # one other.
        blocks_above = blocks_below(tower, block, block_number + 1, True)
        if all(len(blocks_below(tower, blocks[a-1], a)) != 1 for a in blocks_above):
            total += 1
    return total
