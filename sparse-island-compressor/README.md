# sparse-island-compressor

**Day:** 3

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers representing terrain heights where zero represents empty space and non-zero values represent terrain blocks, shift all non-zero blocks to the left to fill in any gaps (zeros) while preserving their relative order.

## Examples

### Input

[0, 3, 0, 1, 4, 0, 2]

### Output

[3, 1, 4, 2, 0, 0, 0]

### Explanation

The non-zero blocks 3, 1, 4, 2 are shifted to the front, and the remaining spaces are filled with zeros.

### Input

[0, 0, 0]

### Output

[0, 0, 0]

### Explanation

Since there are no non-zero elements, the array remains all zeros.

## Constraints

- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000


## Complexity

**Time Complexity:** O(N) where N is the length of the array

**Space Complexity:** O(1) as the modification is done in-place
