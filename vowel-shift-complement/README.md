# vowel-shift-complement

**Day:** 27

**Difficulty:** Easy

**Category:** Strings

## Problem

Given a string, extract all its vowels in order of appearance, reverse them, and place them back into the exact vowel positions of the original string while leaving all consonants untouched.

## Examples

### Input

s = "leetcode"

### Output

"leotcede"

### Explanation

The vowels in 'leetcode' are e, e, o, e. Reversed, they become e, o, e, e. Replacing the vowels at their original indices yields 'leotcede'.

### Input

s = "hello"

### Output

"holle"

### Explanation

The vowels are e, o. Reversed they are o, e. Replacing them gives 'holle'.

## Constraints

- s consists of lowercase English letters only.
- Length of s is between 1 and 1000.


## Complexity

**Time Complexity:** O(N) where N is the length of the string

**Space Complexity:** O(N) to store the character list and extracted vowels
