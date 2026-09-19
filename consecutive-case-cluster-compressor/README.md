# consecutive-case-cluster-compressor

**Day:** 24

**Difficulty:** Easy

**Category:** Strings

## Problem

Given a string, compress groups of consecutive lowercase characters and groups of consecutive uppercase characters by replacing each consecutive block with the character case type indicator ('L' or 'U') followed by the length of the block.

## Examples

### Input

s = "aAABbbcc"

### Output

"L1U3L1U1L3"

### Explanation

The string breaks down into: 'a' (lowercase, len 1 -> L1), 'AAB' (uppercase, len 3 -> U3), 'b' (lowercase, len 1 -> L1), 'B' (uppercase, len 1 -> U1), 'cc' (lowercase, len 2 -> L3 wait, 'bbcc' is lowercase len 4 -> L4). Let's re-eval: 'a'->L1, 'AAB'->U3, 'bbcc'->L4. Result: L1U3L4.

## Constraints

- 1 <= len(s) <= 1000
- s consists only of uppercase and lowercase English letters.


## Complexity

**Time Complexity:** O(N) where N is the length of the string.

**Space Complexity:** O(N) to store the result string.
