from itertools import chain
from copy import deepcopy

def create_tower(blocks):
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

def blocks_below(tower, block, above=False):
    """returns the blocks above or below the given block"""
    below = set()


    if not above:
        if block in list(chain.from_iterable(tower[0])):
            return below

        for z, s in enumerate(tower[1:]):
            for y, r in enumerate(s):
                for x, b in enumerate(r):
                    block_below = tower[z][y][x]
                    if b == block and block_below not in [False, b]:
                        below.add(block_below)

        return below

    else:
        if block in list(chain.from_iterable(tower[-1])):
            return below

        for z, s in enumerate(tower[:-1]):
            for y, r in enumerate(s):
                for x, b in enumerate(r):
                    block_above = tower[z+1][y][x]
                    if b == block and block_above not in [False, b]:
                        below.add(block_above)
        
        return below

def fall_blocks(blocks):
    prev_blocks = []
    while prev_blocks != blocks:
        prev_blocks = deepcopy(blocks)
        tower = create_tower(blocks)
        for block, coords in enumerate(blocks):
            if len(blocks_below(tower, block + 1)) == 0 and coords[0][2] != 0:
                coords[0][2] -= 1
                coords[1][2] -= 1

    return blocks
