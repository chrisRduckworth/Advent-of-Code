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
