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
    
"""
give the verifactin function the full 3 rows
also give it the index of the gear youre checking (in case there's multiple)
check sides and find the numbers if they exist (this is all regex)
get three characters above/below gear
it's 0, 1, or 2 numbers 
if it's 0 then done
if it's 1 you can either see:
    the beginning, in which case you can regex to find it 
    the end, in which case you can regex to find it 
    both, in which case find all matches for numbers on that line,
        then find the match where the index of the gear is between start and end
if it's 2 then you can just find them 
"""

def find_gear_ratio(index, rows):
    # why did i not just pad beginning/end of each row with a dot to compensate
    # for when the thing starts at a start/end
    numbers = []
    if rows[1][index - 1] in "0123456789":
        # slice or row[1] ending at index [index]
        numbers.append(int(re.search(r"\d+$", rows[1][:index])[0]))
    if rows[1][index + 1] in "0123456789":
        numbers.append(int(re.search(r"^\d+", rows[1][index + 1:])[0]))

    # now top/bottom 
    top_3 = rows[0][index - 1: index + 2]
    if top_3 == "...":
        # do nothing
        pass
    elif re.search(r"\d\.\d", top_3) is not None:
        # there are two numbers
        # find top elft
        numbers.append(int(re.search(r"\d+$", rows[0][:index])[0]))
        # find top right 
        numbers.append(int(re.search(r"^\d+", rows[0][index + 1:])[0]))
    else:
        # there is precisely one number:
        # n.. nn. nnn .nn ..n 
        if re.search(r"\.\d", top_3) is not None:
            numbers.append(int(re.search(r"\d+", rows[0][index:])[0]))
        elif re.search(r"\d\.", top_3) is not None:
            numbers.append(int(re.findall(r"\d+", rows[0][:index + 1])[-1]))
        else:
            matches = re.finditer(r"\d+", rows[0])
            for match in matches:
                if match.start() < index and match.end() > index + 1:
                    numbers.append(int(match[0]))
                    break

    bottom_3 = rows[2][index - 1: index + 2]
    if bottom_3 == "...":
        pass
    elif re.search(r"\d\.\d", bottom_3) is not None:
        numbers.append(int(re.search(r"\d+$", rows[2][:index])[0]))
        numbers.append(int(re.search(r"^\d+", rows[2][index + 1:])[0]))
    else:
        if re.search(r"\.\d", bottom_3) is not None:
            numbers.append(int(re.search(r"\d+", rows[2][index:])[0]))
        elif re.search(r"\d\.", bottom_3) is not None:
            numbers.append(int(re.findall(r"\d+", rows[2][:index + 1])[-1]))
        else:
            matches = re.finditer(r"\d+", rows[2])
            for match in matches:
                if match.start() < index and match.end > index + 1:
                    numbers.append(int(match[0]))
                    break
    print(numbers, "< numbers")
    if len(numbers) != 2:
        return 0
        
    else:
        return numbers[0] * numbers[1]
    return 0
    pass

def sum_gear_ratios(schematic):
    pass

if __name__ == "__main__":
    with open("inputs/day_3.txt") as f:
        schematic = f.read()
        total = sum_part_numbers(schematic)
        print(total)
