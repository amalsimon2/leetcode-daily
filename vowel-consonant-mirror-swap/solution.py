def solve(s: str) -> str:
    vowels = set('aeiou')
    extracted_vowels = [c for c in s if c in vowels]
    extracted_vowels.reverse()
    
    res = []
    v_idx = 0
    for c in s:
        if c in vowels:
            res.append(extracted_vowels[v_idx])
            v_idx += 1
        else:
            res.append(c)
            
    return ''.join(res)
