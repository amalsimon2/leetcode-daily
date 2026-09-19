def solve(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_case = 'L' if s[0].islower() else 'U'
    count = 0
    
    for char in s:
        char_case = 'L' if char.islower() else 'U'
        if char_case == current_case:
            count += 1
        else:
            result.append(f"{current_case}{count}")
            current_case = char_case
            count = 1
            
    result.append(f"{current_case}{count}")
    return "".join(result)
