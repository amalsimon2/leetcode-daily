# trough-point-counter

**Day:** 20

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers, count the number of strict trough points. A strict trough point is an element that is strictly less than both of its immediate neighbors. For the boundary elements, they are considered trough points if they are strictly less than their single available neighbor.

## Examples

### Input

[3, 1, 4, 1, 5]

### Output

2

### Explanation

Indices 1 (value 1, neighbors 3 and 4) and 3 (value 1, neighbors 4 and 5) are strict troughs.

### Input

[2, 2, 2]

### Output

0

### Explanation

No element is strictly less than its neighbors.

## Constraints

- 1 <= nums.length <= 1000
- -10^4 <= nums[i] <= 10^4


## Complexity

**Time Complexity:** O(N)

**Space Complexity:** O(1)
