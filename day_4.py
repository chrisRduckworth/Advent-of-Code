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

def find_total_scratchcards(scratchcards):
    scratchcards = scratchcards.splitlines()

    scratchcard_count = {i: 1 for i in range(1, len(scratchcards) + 1)}

    for i, card in enumerate(scratchcards):
        card_number = i + 1
        winning_numbers, your_numbers = card.split("|")
        winning_numbers = re.findall(r"\d+", winning_numbers)[1:]
        your_numbers = re.findall(r"\d+", your_numbers)
        matches = 0
        for number in your_numbers:
            if number in winning_numbers:
                matches += 1 
        for j in range(1, matches + 1):
            if card_number + j <= len(scratchcards):
                scratchcard_count[card_number + j] += scratchcard_count[card_number]

    return sum(scratchcard_count.values())

if __name__ == "__main__":
    with open("inputs/day_4.txt") as f:
        scratchcards = f.read()
        total = sum_scratchcard_points(scratchcards)
        print(total, "< scratchcard points")
        total_scratchcards = find_total_scratchcards(scratchcards)
        print(total_scratchcards, "< total_scratchcards")
