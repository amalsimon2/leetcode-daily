def solve(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_case = 'U' if s[0].isupper() else 'L'
    current_len = 0
    
    for char in s:
        char_case = 'U' if char.isupper() else 'L'
        if char_case == current_case:
            current_len += 1
        else:
            result.append(f"{current_case}{current_len}")
            current_case = char_case
            current_len = 1
            
    result.append(f"{current_case}{current_len}")
    return "".join(result)
