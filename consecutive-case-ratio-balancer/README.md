# consecutive-case-ratio-balancer

**Day:** 28

**Difficulty:** Easy

**Category:** Strings

## Problem

Given a string containing letters, find the longest contiguous substring where the ratio of uppercase to lowercase letters is exactly equal to 1:1, returning the length of that substring.

## Examples

### Input

s = "aAbBcC"

### Output

6

### Explanation

The entire string has 3 uppercase and 3 lowercase letters, perfectly balanced.

### Input

s = "aAaaBb"

### Output

4

### Explanation

The substring "aAaB" or "AaaB" has length 4 with 2 uppercase and 2 lowercase letters.

## Constraints

- 1 <= len(s) <= 1000
- s consists of English letters only (uppercase and lowercase)


## Complexity

**Time Complexity:** O(N^2)

**Space Complexity:** O(1)
