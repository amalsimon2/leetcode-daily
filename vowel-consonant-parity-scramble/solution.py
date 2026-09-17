def solve(s: str) -> str:
    vowels = set('aeiou')
    v_list = []
    c_list = []
    for char in s:
        if char in vowels:
            v_list.append(char)
        else:
            c_list.append(char)
    return "".join(v_list + c_list)
