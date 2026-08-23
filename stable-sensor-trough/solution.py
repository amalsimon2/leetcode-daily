def solve(readings):
    from collections import Counter
    counts = Counter(readings)
    max_repeated = -1
    for num, count in counts.items():
        if count >= 2:
            if num > max_repeated:
                max_repeated = num
    return max_repeated
