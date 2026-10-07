# Explanation

We iterate through each character of the input string. If the character is in the set of vowels ('a', 'e', 'i', 'o', 'u'), we wrap it in parentheses. Otherwise, we wrap it in square brackets. Finally, we join all the wrapped substrings together into a single string.

## Time Complexity

O(N) where N is the length of the string s.

## Space Complexity

O(N) to store the resulting list of wrapped characters.
