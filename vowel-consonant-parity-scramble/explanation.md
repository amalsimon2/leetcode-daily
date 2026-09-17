# Explanation

The algorithm iterates through the input string once, classifying each character as either a vowel ('a', 'e', 'i', 'o', 'u') or a consonant. Vowels and consonants are collected into two separate lists while preserving their original relative order. Finally, the two lists are concatenated and joined into a single string.

## Time Complexity

O(N) where N is the length of the string

## Space Complexity

O(N) to store the characters in lists
