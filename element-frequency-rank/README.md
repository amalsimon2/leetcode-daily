# element-frequency-rank

**Day:** 15

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers, transform each element into its frequency rank. The rank is determined by the element's frequency in the array, where lower frequencies get smaller rank numbers (starting from 1). Elements with the exact same frequency must receive the same rank. If frequencies are different, the element with the lower frequency gets the strictly smaller rank.

## Examples

### Input

[4, 2, 4, 3, 2, 4]

### Output

[3, 1, 3, 2, 1, 3]

### Explanation

Frequencies: 3 appears 3 times (freq 3), 2 appears 2 times (freq 2), 4 appears 3 times (freq 3, wait: 4 appears 3 times, 2 appears 2 times, 3 appears 1 time. Unique frequencies sorted: {1: 3, 2: 2, 4: 3}. Let's re-evaluate: frequencies are 3 (for element 4), 2 (for element 2), 1 (for element 3). Sorted unique frequencies: [1, 2, 3]. Ranks: freq 1 -> rank 1 (element 3), freq 2 -> rank 2 (element 2), freq 3 -> rank 3 (element 4). Thus element 4 gets rank 3, element 2 gets rank 2, element 3 gets rank 1. Resulting array: [3, 2, 3, 1, 2, 3].

## Constraints

- 1 <= nums.length <= 1000
- -10^4 <= nums[i] <= 10^4


## Complexity

**Time Complexity:** O(N log N)

**Space Complexity:** O(N)
