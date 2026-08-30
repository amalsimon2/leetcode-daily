# pivot-equilibrium-finder

**Day:** 10

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers, find the first index where the sum of elements strictly to the left of the index equals the sum of elements strictly to the right of the index. If no such index exists, return -1.

## Examples

### Input

nums = [1, 7, 3, 6, 5, 6]

### Output

3

### Explanation

At index 3, left sum = 1 + 7 + 3 = 11, and right sum = 5 + 6 = 11.

### Input

nums = [1, 2, 3]

### Output

-1

### Explanation

There is no index that satisfies the equilibrium condition.

## Constraints

- 1 <= nums.length <= 10^4
- -1000 <= nums[i] <= 1000


## Complexity

**Time Complexity:** O(n)

**Space Complexity:** O(1)
