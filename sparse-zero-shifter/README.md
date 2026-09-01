# sparse-zero-shifter

**Day:** 11

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers, shift all zeros to the end of the array while maintaining the relative order of the non-zero elements, and return the modified array in-place.

## Examples

### Input

[0, 1, 0, 3, 12]

### Output

[1, 3, 12, 0, 0]

### Explanation

Non-zero elements 1, 3, and 12 maintain their relative order, and the two zeros are moved to the end.

### Input

[0, 0, 1]

### Output

[1, 0, 0]

### Explanation

Zeros are grouped at the end while preserving the single non-zero element.

## Constraints

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4


## Complexity

**Time Complexity:** O(N) where N is the length of the array

**Space Complexity:** O(1) as the transformation is done in-place
