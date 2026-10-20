# vowel-consonant-cluster-toggle

**Day:** 29

**Difficulty:** Easy

**Category:** Strings

## Problem

Given a string of lowercase letters, group consecutive characters into contiguous runs of vowels and consonants. For each run, if its length is even, toggle all its characters to uppercase; if its length is odd, leave them as lowercase. Return the modified string.

## Examples

### Input

s = "programming"

### Output

"prOGRAMmIng"

### Explanation

Runs: 'p' (odd -> 'p'), 'r' (odd -> 'r'), 'o' (odd -> 'o'), 'gr' (len 2, even -> 'GR'), 'a' (odd -> 'a'), 'mm' (len 2, even -> 'MM'), 'i' (odd -> 'i'), 'ng' (len 2, even -> 'NG'). Wait, let's trace: 'p'(1)->p, 'r'(1)->r, 'o'(1)->o, 'gr'(2)->GR, 'a'(1)->a, 'mm'(2)->MM, 'i'(1)->i, 'ng'(2)->NG. Result: p r o GR a MM i NG -> proGRaMMiNG. Wait, let's define vowels: a, e, i, o, u.

## Constraints

- s consists only of lowercase English letters ('a'-'z')
- 1 <= len(s) <= 1000


## Complexity

**Time Complexity:** O(N) where N is the length of the string

**Space Complexity:** O(N) to store the runs and the resulting string
