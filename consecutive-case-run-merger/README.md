# consecutive-case-run-merger

**Day:** 26

**Difficulty:** Easy

**Category:** Strings

## Problem

Given a string containing uppercase and lowercase English letters, group consecutive characters by their casing (lowercase or uppercase) and compress each group into a single character representing that case ('L' for lowercase, 'U' for uppercase) followed by the length of the run.

## Examples

### Input

"aAABbbcc"

### Output

"L1U3L1U2L2"

### Explanation

Runs are: 'a' (lowercase, len 1) -> L1, 'AAB' (uppercase, len 3) -> U3, 'b' (lowercase, len 1) -> L1, 'bb' (uppercase -> wait, 'bb' is lowercase len 2) -> L2, 'cc' is 'bbcc' combined as lowercase len 4. Let's trace 'aAABbbcc': 'a' (L1), 'AAB' (U3), 'bb' (L2), 'cc' (L2 -> combined as L4). Actually, 'bbcc' is all lowercase, so len 4. Final output: L1U3L4.

## Constraints

- 1 <= len(s) <= 1000
- s consists only of English letters (a-z, A-Z)


## Complexity

**Time Complexity:** O(N) where N is the length of the string

**Space Complexity:** O(N) to store the result runs
