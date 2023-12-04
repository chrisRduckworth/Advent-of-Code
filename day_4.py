import re

def sum_scratchcard_points(scratchcards):
    """returns total number of scratchcard points"""
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
    """returns the total number of scratchcards"""
    scratchcards = scratchcards.splitlines()

    # start with one of every card
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

        # each of your numbers that is a winner adds one to the count of
        # the next cards
        for j in range(1, matches + 1):
            if card_number + j <= len(scratchcards):
                # each card adds its own count to subsequent cards for the match
                # eg if you have 3 card 1s, then each increases card 2 by 1,
                # so the number of card 2s increases by 3
                scratchcard_count[card_number + j] += scratchcard_count[card_number]

    return sum(scratchcard_count.values())

if __name__ == "__main__":
    with open("inputs/day_4.txt") as f:
        scratchcards = f.read()
        total = sum_scratchcard_points(scratchcards)
        print(total, "< scratchcard points")
        total_scratchcards = find_total_scratchcards(scratchcards)
        print(total_scratchcards, "< total_scratchcards")
