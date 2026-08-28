# array-parity-boundary

**Day:** 7

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers, rearrange its elements in-place such that all even numbers appear before all odd numbers, and return the modified array. Furthermore, the relative order of even numbers and odd numbers among themselves should be preserved.

## Examples

### Input

nums = [3, 1, 2, 4]

### Output

[2, 4, 3, 1]

### Explanation

Even numbers 2 and 4 are moved to the front while preserving their relative order, followed by odd numbers 3 and 1.

### Input

nums = [1, 3, 5]

### Output

[1, 3, 5]

### Explanation

There are no even numbers, so the array remains unchanged.

## Constraints

- 1 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000


## Complexity

**Time Complexity:** O(N) where N is the length of the array

**Space Complexity:** O(N) to store the separated even and odd sublists
