import numpy as np

def compare_mirrored(pattern, k, column_or_row):
    """compares a mirrored version around the k-th column/row"""
    length = len(pattern) if column_or_row == "row" else len(pattern[0])
    start_index = max(0, - len(pattern) + 2 * k)
    end_index = min(len(pattern), 2 * k)
    if column_or_row == "row":
        slice_to_compare = pattern[start_index: end_index]
        mirrored_slice = np.flipud(np.copy(slice_to_compare))
    else:
        slice_to_compare = [row[start_index:end_index] for row in pattern]
        mirrored_slice = np.fliplr(np.copy(slice_to_compare))
    return np.array_equal(slice_to_compare, mirrored_slice)
