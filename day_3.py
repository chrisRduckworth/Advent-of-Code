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
    pass 
