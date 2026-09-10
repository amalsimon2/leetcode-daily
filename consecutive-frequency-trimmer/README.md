# consecutive-frequency-trimmer

**Day:** 19

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers, remove any element that appears consecutively strictly fewer times than a given threshold k, and return the modified array.

## Examples

### Input

nums = [1, 1, 2, 2, 2, 3, 1, 1], k = 2

### Output

[1, 1, 2, 2, 2, 1, 1]

### Explanation

The element 3 appears consecutively 1 time, which is less than k=2. It is removed. All other consecutive runs have a length of at least 2.

## Constraints

- 1 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000
- 1 <= k <= 1000


## Complexity

**Time Complexity:** O(N)

**Space Complexity:** O(N)
