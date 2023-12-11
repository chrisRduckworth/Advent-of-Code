def expand_space(image, char="."):
    """adds empty lines for each row/column with no galaxy"""
    for i in range(len(image) - 1, -1, -1):
        if image[i] == "." * len(image[0]):
            image.insert(i, char * len(image[0]))
    for i in range(len(image[0]) - 1, -1, -1):
        if all(row[i] in [".", char] for row in image):
            image = [row[:i] + char + row[i:] for row in image]
    return image

def find_distance(image, space_size, galaxy_1, galaxy_2):
    """finds the distance between 2 galaxies"""
    change_x = abs(galaxy_1[0] - galaxy_2[0])
    change_y = abs(galaxy_1[1] - galaxy_2[1])

    start_galaxy_x = min(galaxy_1, galaxy_2, key=lambda x: x[0])
    start_galaxy_y = min(galaxy_1, galaxy_2, key=lambda x: x[1])

    # first find path along x-axis
    x_string = image[start_galaxy_x[1]][start_galaxy_x[0] + 1: start_galaxy_x[0] + change_x]

    # then path along y axis
    rows = image[start_galaxy_y[1]: start_galaxy_y[1] + change_y + 1]
    y_string = "".join(row[start_galaxy_x[0] + change_x] for row in rows)
    
    shortest_path = x_string + y_string

    # use space_size - 1 because we're already including it once in the 
    # len(shortest_path)
    if change_x == 0:
        # because otherwise you count the start twice
        return len(shortest_path) - 1 + (space_size - 1) * (shortest_path.count("@"))
    return len(shortest_path) + (space_size - 1) * (shortest_path.count("@"))

def sum_shortest_distances(image, space_size = 1):
    """finds the sum of the shortest distances between all galaxies"""
    image = image.splitlines()
    image = expand_space(image, "@")

    # create a list of all galaxies
    galaxies = []
    for y, row in enumerate(image):
        for x, char in enumerate(row):
            if char == "#":
                galaxies.append((x,y))

    total_distance = 0
    for i, galaxy in enumerate(galaxies):
        # for each galaxy, calculate distance from itself to each galaxy
        # after itself in the list
        for end_galaxy in galaxies[i+1:]:
            total_distance += find_distance(image, space_size, galaxy, end_galaxy)

    return total_distance

if __name__ == "__main__":
    with open("inputs/day_11.txt") as f:
        image = f.read()
        distance = sum_shortest_distances(image)
        print(distance, "< sum of shortest distances")
