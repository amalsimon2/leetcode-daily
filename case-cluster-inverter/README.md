# case-cluster-inverter

**Day:** 23

**Difficulty:** Easy

**Category:** Strings

## Problem

Given a string containing letters and other characters, identify contiguous clusters of alphabetic characters. If a cluster contains more uppercase letters than lowercase letters, convert the entire cluster to uppercase; otherwise, convert the entire cluster to lowercase. Non-alphabetic characters remain unchanged and act as cluster separators.

## Examples

### Input

AbC-dEfG!HI

### Output

ABC-defg!HI

### Explanation

Clusters are: 'AbC' (2 upper, 1 lower -> becomes 'ABC'), 'dEfG' (2 upper, 2 lower -> tie or <= lower becomes 'defg'), 'HI' (2 upper, 0 lower -> becomes 'HI'). Separators '-' and '!' remain.

## Constraints

- s consists of printable ASCII characters.
- Length of s is between 1 and 1000.


## Complexity

**Time Complexity:** O(N) where N is the length of the string.

**Space Complexity:** O(N) to store the resulting character list and final string.
