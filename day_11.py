def expand_space(image):
    for i in range(len(image) - 1, -1, -1):
        if image[i] == "." * len(image[0]):
            image.insert(i, "." * len(image[0]))
    for i in range(len(image[0]) - 1, -1, -1):
        if all(row[i] == "." for row in image):
            image = [row[:i] + "." + row[i:] for row in image]
    return image

def sum_shortest_distances(image):
    image = image.splitlines()
    image = expand_space(image)

    galaxies = []
    for y, row in enumerate(image):
        for x, char in enumerate(row):
            if char == "#":
                galaxies.append((x,y))

    total_distance = 0
    for i, galaxy in enumerate(galaxies):
        for end_galaxy in galaxies[i+1:]:
            total_distance += abs(galaxy[0] - end_galaxy[0]) + abs(galaxy[1] - end_galaxy[1])

    return total_distance
