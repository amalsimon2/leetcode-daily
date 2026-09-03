# alternating-sum-balance

**Day:** 13

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers, find the index where removing that element results in an alternating sum balance, where the alternating sum of the remaining elements from the left equals the alternating sum from the right up to that point, or return -1 if no such index exists.

## Examples

### Input

nums = [2, -1, 2]

### Output

1

### Explanation

If we remove index 1 (value -1), the remaining array is [2, 2]. The alternating sum of [2] on the left (2) equals the alternating sum on the right [2] (2).

### Input

nums = [1, 2, 3]

### Output

-1

### Explanation

No removal creates an alternating sum balance.

## Constraints

- 1 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000


## Complexity

**Time Complexity:** O(N^2)

**Space Complexity:** O(N)
