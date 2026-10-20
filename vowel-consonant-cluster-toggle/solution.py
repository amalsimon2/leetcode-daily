def solve(s: str) -> str:
    if not s:
        return ""
    
    vowels = set("aeiou")
    
    def is_vowel(c):
        return c in vowels
    
    runs = []
    curr_run = [s[0]]
    curr_is_v = is_vowel(s[0])
    
    for char in s[1:]:
        if is_vowel(char) == curr_is_v:
            curr_run.append(char)
        else:
            runs.append("".join(curr_run))
            curr_run = [char]
            curr_is_v = is_vowel(char)
    runs.append("".join(curr_run))
    
    result = []
    for run in runs:
        if len(run) % 2 == 0:
            result.append(run.upper())
        else:
            result.append(run)
            
    return "".join(result)
