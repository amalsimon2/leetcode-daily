def solve(s: str) -> int:
    max_len = 0
    n = len(s)
    for i in range(n):
        upper_count = 0
        lower_count = 0
        for j in range(i, n):
            if s[j].isupper():
                upper_count += 1
            else:
                lower_count += 1
            if upper_count == lower_count:
                max_len = max(max_len, j - i + 1)
    return max_len
