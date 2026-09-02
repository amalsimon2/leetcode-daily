# monotonic-streak-counter

**Day:** 12

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers, find the length of the longest contiguous subsegment where the elements are strictly increasing or strictly decreasing.

## Examples

### Input

nums = [1, 2, 3, 2, 1, 4, 5]

### Output

3

### Explanation

The longest monotonic streaks are [1, 2, 3] (increasing of length 3) and [3, 2, 1] (decreasing of length 3). The maximum length is 3.

### Input

nums = [5, 5, 5, 5]

### Output

1

### Explanation

With all elements equal, no strict monotonic streak can exceed length 1.

## Constraints

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9


## Complexity

**Time Complexity:** O(N) where N is the length of the input array

**Space Complexity:** O(1)
