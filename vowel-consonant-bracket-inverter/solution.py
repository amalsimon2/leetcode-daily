def solve(s: str) -> str:
    vowels = set('aeiou')
    result = []
    for char in s:
        if char in vowels:
            result.append(f"({char})")
        else:
            result.append(f"[{char}]")
    return "".join(result)
