# symmetric-edge-trimmer

**Day:** 9

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers and a target value, repeatedly remove elements from both the absolute left and right ends of the array as long as they match the target value. Return the length of the remaining array.

## Examples

### Input

arr = [3, 2, 3, 4, 3, 3], target = 3

### Output

3

### Explanation

The elements at both ends matching 3 are trimmed. Leftmost 3 and rightmost two 3s are removed, leaving [2, 4, 3] of length 3.

### Input

arr = [5, 5, 5], target = 5

### Output

0

### Explanation

All elements match the target and are trimmed, leaving an empty array of length 0.

## Constraints

- 0 <= arr.length <= 10^5
- -10^4 <= arr[i], target <= 10^4


## Complexity

**Time Complexity:** O(N) where N is the length of the array

**Space Complexity:** O(1)
