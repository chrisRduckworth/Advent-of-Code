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

def find_zero_value(subsequences):
    """returns zero-th value of the sequence"""
    subsequences[-1].insert(0, subsequences[-1][0])
    for i in range(len(subsequences) - 2, -1, -1):
        subsequences[i].insert(0, subsequences[i][0] - subsequences[i + 1][0])
    return subsequences[0][0]

def sum_extrapolated_values(report, zeros=False):
    sequences = [[int(n) for n in seq.split()] for seq in report.splitlines()]
    subsequences = [find_subsequences(seq) for seq in sequences]
    if zeros:
        values = [find_zero_value(sub) for sub in subsequences]
    else:
        values = [find_next_value(sub) for sub in subsequences]
    return sum(values)

if __name__ == "__main__":
    with open("inputs/day_9.txt") as f:
        report = f.read()
        sums = sum_extrapolated_values(report)
        print(sums, "< sum of sum of extrapolated values")
