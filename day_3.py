import re

def has_adjacent_symbol(start_index, length, rows):
    top_characters = rows[0][start_index - 1:start_index + length + 1]
    bottom_characters = rows[2][start_index - 1:start_index + length + 1]
    left_character = rows[1][start_index - 1]
    right_character = rows[1][start_index + length]
    adjacent_characters = top_characters + left_character + right_character + bottom_characters

    return re.search(r"[^.]", adjacent_characters) is not None

def sum_part_numbers(schematic):
    pass 
