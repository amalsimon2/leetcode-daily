def solve(s: str) -> str:
    vowels = "aeiouAEIOU"
    s_list = list(s)
    extracted_vowels = [char for char in s_list if char in vowels]
    extracted_vowels.reverse()
    
    vowel_idx = 0
    for i in range(len(s_list)):
        if s_list[i] in vowels:
            s_list[i] = extracted_vowels[vowel_idx]
            vowel_idx += 1
            
    return "".join(s_list)
