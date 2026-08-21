def solve(chars):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowel_indices = []
    vowel_chars = []
    
    for i, ch in enumerate(chars):
        if ch in vowels:
            vowel_indices.append(i)
            vowel_chars.append(ch)
            
    if not vowel_indices:
        return chars
        
    # Shift vowels right cyclically by 1
    shifted_vowels = [vowel_chars[-1]] + vowel_chars[:-1]
    
    result = list(chars)
    for idx, ch in zip(vowel_indices, shifted_vowels):
        result[idx] = ch
        
    return result
