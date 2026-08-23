# stable-sensor-trough

**Day:** 4

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integer sensor readings, find the maximum reading that appears at least twice in the array. If no reading appears at least twice, return -1.

## Examples

### Input

readings = [4, 7, 2, 7, 4, 9, 4]

### Output

7

### Explanation

The numbers 4 and 7 both appear multiple times. The maximum of these is 7.

### Input

readings = [1, 2, 3, 5]

### Output

-1

### Explanation

No number appears more than once.

## Constraints

- 1 <= len(readings) <= 10^5
- -10^9 <= readings[i] <= 10^9


## Complexity

**Time Complexity:** O(N) where N is the length of the readings array.

**Space Complexity:** O(N) to store the frequency counts.
