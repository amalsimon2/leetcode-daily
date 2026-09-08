# subarray-cap-bounded-product

**Day:** 17

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of positive integers and an integer cap, count the total number of non-empty contiguous subarrays whose maximum element is less than or equal to the cap.

## Examples

### Input

nums = [2, 1, 3, 2], cap = 2

### Output

4

### Explanation

The valid contiguous subarrays are [2], [1], [3 is invalid], [2], and [2, 1]. Wait, [2, 1] max is 2 (<=2). Subarrays: [2] (len 1), [1] (len 1), [2] (len 1), [2, 1] (len 2). Total = 4.

## Constraints

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
- 1 <= cap <= 10^6


## Complexity

**Time Complexity:** O(N)

**Space Complexity:** O(1)
