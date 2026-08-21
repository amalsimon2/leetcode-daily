# vowel-vanguard-shift

**Day:** 2

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given a list of characters, identify all vowels (a, e, i, o, u, case-insensitive) and shift their positions cyclically to the right by one among themselves, while keeping all consonants in their original positions.

## Examples

### Input

chars = ['p', 'y', 't', 'h', 'o', 'n']

### Output

['p', 'y', 't', 'h', 'o', 'n']

### Explanation

There is only one vowel 'o', so shifting it results in the same list.

### Input

chars = ['a', 'b', 'e', 'c', 'i']

### Output

['i', 'b', 'a', 'c', 'e']

### Explanation

The vowels are 'a', 'e', 'i'. Shifting them right cyclically places 'i' at index 0, 'a' at index 2, and 'e' at index 4.

## Constraints

- 1 <= len(chars) <= 10^4
- chars contains lowercase and/or uppercase English letters


## Complexity

**Time Complexity:** O(N) where N is the length of the character array

**Space Complexity:** O(N) to store the vowel tracking lists and the result array
