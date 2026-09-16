# vowel-consonant-mirror-swap

**Day:** 21

**Difficulty:** Easy

**Category:** Strings

## Problem

Given a string of lowercase English letters, reverse the sequence of all vowels in the string while keeping all consonants in their exact original positions.

## Examples

### Input

s = "leetcode"

### Output

"leotcede"

### Explanation

The vowels in 'leetcode' are e, e, o, e. Reversing them gives e, o, e, e. Placed back into the vowel positions, we get 'leotcede'.

### Input

s = "hello"

### Output

"holle"

### Explanation

The vowels are e, o. Reversing them gives o, e. Result is 'holle'.

## Constraints

- 1 <= s.length <= 1000
- s consists only of lowercase English letters ('a', 'e', 'i', 'o', 'u' are vowels).


## Complexity

**Time Complexity:** O(N) where N is the length of the string, as we traverse the string a constant number of times.

**Space Complexity:** O(N) to store the extracted vowels and the resulting string characters.
