import re

def has_adjacent_symbol(start_index, length, rows):
    """returns true if the adjacent characters have a symbol"""
    bounding_box = (max(start_index - 1, 0), min(start_index + length + 1, len(rows[0])))
    
    top_characters = rows[0][bounding_box[0]: bounding_box[1]]
    bottom_characters = rows[2][bounding_box[0]: bounding_box[1]]
    if start_index > 0:
        left_character = rows[1][start_index - 1]
    else:
        left_character = "" 
    if start_index + length < len(rows[0]):
        right_character = rows[1][start_index + length]
    else:
        right_character = ""
        
    adjacent_characters = top_characters + left_character + right_character + bottom_characters

    return re.search(r"[^.]", adjacent_characters) is not None

def sum_part_numbers(schematic):
    """finds the sum of all valid numbers in the shcematic"""
    lines = schematic.splitlines()
    total = 0
    
    # first row
    first_row_numbers = re.finditer(r"\d+", lines[0])
    for number in first_row_numbers:
        start_index = number.start()
        length = number.end() - number.start()
        rows = ["." * len(lines[0]), lines[0], lines[1]]
        if has_adjacent_symbol(start_index, length, rows):
            total += int(number[0])
    
    # middle rows
    for i in range(1, len(lines) - 1):
        line = lines[i]
        numbers = re.finditer(r"\d+", line)
        for number in numbers:
            start_index = number.start()
            length = number.end() - number.start()
            rows = lines[i - 1: i + 2]
            if has_adjacent_symbol(start_index, length, rows):
                total += int(number[0])
    
    # last row 
    last_row_numbers = re.finditer(r"\d+", lines[-1])
    for number in last_row_numbers:
        start_index = number.start()
        length = number.end() - number.start()
        rows = [lines[-2], lines[-1], "." * len(lines[-1])]
        if has_adjacent_symbol(start_index, length, rows):
            total += int(number[0])

    return total
    
