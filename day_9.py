def find_subsequences(sequence):
    if all(n == sequence[0] for n in sequence):
        return [sequence]
    differences = [sequence[i + 1] - sequence[i] for i in range(0, len(sequence) - 1)]
    return [sequence, *find_subsequences(differences)]

def sum_extrapolated_values(report):
    pass
