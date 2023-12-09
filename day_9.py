def find_subsequences(sequence):
    """finds the subsequences from finding differences"""
    if all(n == sequence[0] for n in sequence):
        return [sequence]
    differences = [sequence[i + 1] - sequence[i] for i in range(0, len(sequence) - 1)]
    return [sequence, *find_subsequences(differences)]

def find_next_value(subsequences):
    """returns next value of the sequence"""
    # add an element to the last subsequence (the constant)
    subsequences[-1].append(subsequences[-1][0])
    for i in range(len(subsequences) - 2, -1, -1):
        # new value is sum of previous + below
        subsequences[i].append(subsequences[i][-1] + subsequences[i + 1][-1])
    return subsequences[0][-1]

def sum_extrapolated_values(report):
    sequences = [[int(n) for n in seq.split()] for seq in report.splitlines()]
    subsequences = [find_subsequences(seq) for seq in sequences]
    next_values = [find_next_value(sub) for sub in subsequences]
    return sum(next_values)
