def dig_trench(instructions):
    """creates an array representing the dug trench"""
    # start with a 1x1 grid with a #
    # then for each step:
    # for each dig number:
    # add a hash in that direction, 
    # then an empty column/row in that direction
    
    # will also need to keep track of position
    trenches = [["#"]]
    position = (0,0)

    for instruction in instructions:
        for i in range(instruction[1]):
            if instruction[0] == "R":
                if position[0] + 1 == len(trenches[0]):
                    trenches = [[*row, "."] for row in trenches]
                position = (position[0] + 1, position[1])
                trenches[position[1]][position[0]] = "#"

            elif instruction[0] == "D":
                if position[1] + 1 == len(trenches):
                    trenches.append(["." for c in range(len(trenches[0]))])
                position = (position[0], position[1] + 1)
                trenches[position[1]][position[0]] = "#"

            elif instruction[0] == "L":
                if position[0] == 0:
                    trenches = [[".", *row] for row in trenches]
                trenches[position[1]][position[0]] = "#"

            elif instruction[0] == "U":
                if position[1] == 0:
                    trenches.insert(0, ["." for c in range(len(trenches[0]))])
                trenches[position[1]][position[0]] = "#"

            
    return trenches

# flood fill for filling it up
