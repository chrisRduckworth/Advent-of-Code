import re

def sum_scratchcard_points(scratchcards):
    scratchcards = scratchcards.splitlines()
    total = 0
    for card in scratchcards:
        winning_numbers, your_numbers = card.split("|")
        winning_numbers = re.findall(r"\d+", winning_numbers)[1:]
        your_numbers = re.findall(r"\d+", your_numbers)
        matches = 0
        for number in your_numbers:
            if number in winning_numbers:
                matches += 1 
        if matches > 0:
            total += 2 ** (matches - 1)

    return total

if __name__ == "__main__":
    with open("inputs/day_4.txt") as f:
        scratchcards = f.read()
        total = sum_scratchcard_points(scratchcards)
        print(total, "< scratchcard points")
