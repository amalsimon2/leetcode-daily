# threshold-step-reducer

**Day:** 18

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers and an integer threshold, repeatedly reduce each element in the array by the maximum multiple of the threshold that does not exceed its current value until all elements are strictly less than the threshold. Return the final reduced array.

## Examples

### Input

nums = [12, 5, 18], threshold = 4

### Output

[0, 1, 2]

### Explanation

For 12: 12 - 3*4 = 0. For 5: 5 - 1*4 = 1. For 18: 18 - 4*4 = 2. Result is [0, 1, 2].

### Input

nums = [3, 2, 1], threshold = 5

### Output

[3, 2, 1]

### Explanation

All elements are already less than 5, so no reductions are made.

## Constraints

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000
- 1 <= threshold <= 1000


## Complexity

**Time Complexity:** O(N)

**Space Complexity:** O(N)
