# vowel-consonant-bracket-inverter

**Day:** 25

**Difficulty:** Easy

**Category:** Strings

## Problem

Given a string containing only lowercase letters, wrap every vowel in parentheses '(' and ')' and every consonant in square brackets '[' and ']'.

## Examples

### Input

abc

### Output

(a)[b][c]

### Explanation

'a' is a vowel so it becomes (a), 'b' and 'c' are consonants so they become [b] and [c].

### Input

aeiou

### Output

(a)(e)(i)(o)(u)

### Explanation

All characters are vowels.

## Constraints

- 1 <= s.length <= 100
- s consists only of lowercase English letters ('a' through 'z').


## Complexity

**Time Complexity:** O(N) where N is the length of the string s.

**Space Complexity:** O(N) to store the resulting list of wrapped characters.
