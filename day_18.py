def dig_trench(instructions):
    """creates an array representing the dug trench"""
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
                else:
                    position = (position[0] - 1, position[1])
                trenches[position[1]][position[0]] = "#"

            elif instruction[0] == "U":
                if position[1] == 0:
                    trenches.insert(0, ["." for c in range(len(trenches[0]))])
                else:
                    position = (position[0], position[1] - 1)
                trenches[position[1]][position[0]] = "#"

    return trenches

def fill_trenches(trenches):
    trenches.insert(0, ["."] * len(trenches[0]))
    trenches.append(["." * len(trenches[0])])
    trenches = [[".", *row, "."] for row in trenches]

    for x, char in enumerate(trenches[1]):
        if trenches[2][x] == "." and char == "#":
            start = (x, 2)
            break
    
    def flood_fill(x, y):
        nonlocal trenches
        if trenches[y][x] == "#":
            return
        trenches[y][x] = "#"
        flood_fill(x-1, y)
        flood_fill(x+1, y)
        flood_fill(x, y-1)
        flood_fill(x, y+1)

    flood_fill(*start)

    return [row[1:-1] for row in trenches[1:-1]]

if __name__ == "__main__":
    with open("inputs/day_18.txt") as f:
        instructions = [[i.split()[0], int(i.split()[1]), i.split()[2]] for i in f.read().splitlines()]
        trenches = dig_trench(instructions)
        filled = fill_trenches(trenches)
        filled = "\n".join("".join(r) for r in filled)
        print(filled)
        print(filled.count("#"), "< total dug")
