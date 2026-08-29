# adjacent-polarity-interleave

**Day:** 8

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers containing an equal number of positive and negative integers, rearrange the array such that positive and negative numbers strictly alternate, preserving the relative order of the positive numbers and the relative order of the negative numbers. The array is guaranteed to start with the sign of the first element in the original array.

## Examples

### Input

nums = [3, -1, 2, -5]

### Output

[3, -1, 2, -5]

### Explanation

The array already strictly alternates between positive (3, 2) and negative (-1, -5), maintaining relative order.

### Input

nums = [-2, 3, 1, -1]

### Output

[-2, 3, -1, 1]

### Explanation

Positives are [3, 1] and negatives are [-2, -1]. Interleaving them starting with negative gives [-2, 3, -1, 1].

## Constraints

- 2 <= nums.length <= 1000
- nums.length is even
- Equal number of strictly positive and strictly negative integers (no zeros)
- -1000 <= nums[i] <= 1000
- nums[i] != 0


## Complexity

**Time Complexity:** O(N)

**Space Complexity:** O(N)
