import numpy as np

def compare_mirrored(pattern, k, column_or_row):
    """compares a mirrored version around the k-th column/row"""
    length = len(pattern) if column_or_row == "row" else len(pattern[0])
    start_index = max(0, - length + 2 * k)
    end_index = min(length, 2 * k)
    if column_or_row == "row":
        slice_to_compare = pattern[start_index: end_index]
        mirrored_slice = np.flipud(np.copy(slice_to_compare))
    else:
        slice_to_compare = [row[start_index:end_index] for row in pattern]
        mirrored_slice = np.fliplr(np.copy(slice_to_compare))
    return np.array_equal(slice_to_compare, mirrored_slice)

def make_notes(pattern):
    """sums rows and columns with symmetry"""
    # columns
    total = 0
    for i in range(1, len(pattern[0])):
        if compare_mirrored(pattern, i, "column"):
            total += i
    
    # rows
    for i in range(1, len(pattern)):
        if compare_mirrored(pattern, i, "row"):
            total += i * 100
    return total

def sum_notes(patterns):
    patterns = patterns.split("\n\n")
    patterns = [pattern.splitlines() for pattern in patterns]
    patterns = [[list(row) for row in pattern] for pattern in patterns]
    total = 0
    for pattern in patterns:
        total += make_notes(pattern)
    return total

def make_notes_part_2(pattern):
    matching_columns = []
    for i in range(1, len(pattern[0])):
        if compare_mirrored(pattern, i, "column"):
            matching_columns.append(i)
    
    matching_rows = []
    for i in range(1, len(pattern)):
        if compare_mirrored(pattern, i, "row"):
            matching_rows.append(i)
    return set(matching_columns), set(matching_rows)


def sum_notes_part_two(patterns):
    patterns = patterns.split("\n\n")
    patterns = [pattern.splitlines() for pattern in patterns]
    patterns = [[list(row) for row in pattern] for pattern in patterns]
    total = 0
    for pattern in patterns:
        initial_columns, initial_rows = make_notes_part_2(pattern)
        new_columns, new_rows = [], []
        for i in range(len(pattern) * len(pattern[0])):
            x, y = i % len(pattern[0]), i // len(pattern[0])
            if pattern[y][x] == "#":
                pattern[y][x] = "."
            else:
                pattern[y][x] = "#"
            columns, rows = make_notes_part_2(pattern)
            if pattern[y][x] == "#":
                pattern[y][x] = "."
            else:
                pattern[y][x] = "#"
            for c in columns:
                if c not in initial_columns:
                    new_columns.append(c)
            for r in rows:
                if r not in initial_rows:
                    new_rows.append(r)
        new_columns = set(new_columns)
        new_rows = set(new_rows)
        total += sum(new_columns)
        total += sum(100 * r for r in new_rows)
    return total
    

if __name__ == "__main__":
    with open("inputs/day_13.txt") as f:
        patterns = f.read()
        total_notes = sum_notes(patterns)
        print(total_notes, "< total notes")
        total_changed_notes = sum_notes_part_two(patterns)
        print(total_changed_notes, "< total changed notes")
