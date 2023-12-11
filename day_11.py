def expand_space(image, char="."):
    for i in range(len(image) - 1, -1, -1):
        if image[i] == "." * len(image[0]):
            image.insert(i, char * len(image[0]))
    for i in range(len(image[0]) - 1, -1, -1):
        if all(row[i] in [".", char] for row in image):
            image = [row[:i] + char + row[i:] for row in image]
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

if __name__ == "__main__":
    with open("inputs/day_11.txt") as f:
        image = f.read()
        distance = sum_shortest_distances(image)
        print(distance, "< sum of shortest distances")
