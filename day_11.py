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
    pass
