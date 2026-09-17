# vowel-consonant-parity-scramble

**Day:** 22

**Difficulty:** Easy

**Category:** Strings

## Problem

Given a string of lowercase English letters, rearrange its characters such that all vowels appear first in their relative order of appearance, followed by all consonants in their relative order of appearance.

## Examples

### Input

"algorithm"

### Output

"aoilgrthm"

### Explanation

Vowels are 'a', 'o', 'i' (relative order: a, o, i). Consonants are 'l', 'g', 'r', 't', 'h', 'm' (relative order: l, g, r, t, h, m). Combined they form 'aoilgrthm'.

### Input

"python"

### Output

"opythn"

### Explanation

Vowels are 'o', 'y' (treating 'y' as a consonant unless specified; here 'o' is the only vowel). Consonants are 'p', 'y', 't', 'h', 'n'. Vowels: 'o'. Consonants: 'pythn'. Result: 'opythn'.

## Constraints

- The string s consists only of lowercase English letters.
- The length of s is between 1 and 1000.


## Complexity

**Time Complexity:** O(N) where N is the length of the string

**Space Complexity:** O(N) to store the characters in lists
