import re, math

def find_winning_products(races):
    times, distances = [[int(n) for n in re.findall(r"\d+", l)] for l in races.splitlines()]
    product = 1
    for i in range(0, len(times)):
        minimum_button_press = math.floor((times[i] - math.sqrt(times[i]**2 - 4 * distances[i]))/2) + 1
        max_button_press = math.ceil((times[i] + math.sqrt(times[i]**2 - 4 * distances[i]))/2) - 1
        # we have to include the +/- 1 at the end for the above to deal with integer solutions
        product *= (max_button_press + 1 - minimum_button_press)
    
    return product

if __name__ == "__main__":
    with open("inputs/day_6.txt") as f:
        races = f.read()
        product = find_winning_products(races)
        print(product, " product of number of winning times")
