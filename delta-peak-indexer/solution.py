def solve(readings):
    n = len(readings)
    if n < 3:
        return -1
    for i in range(1, n - 1):
        if readings[i] > readings[i - 1] and readings[i] > readings[i + 1]:
            return i
    return -1
