# delta-peak-indexer

**Day:** 6

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers representing sequential meter readings, find the index of the first element that is strictly greater than both of its immediate neighbors. If no such element exists, return -1.

## Examples

### Input

readings = [1, 3, 2, 4, 1]

### Output

1

### Explanation

At index 1, the value 3 is greater than 1 and 2. (Index 3 also holds a peak 4, but index 1 is the first one).

### Input

readings = [5, 4, 3, 2, 1]

### Output

-1

### Explanation

The array is strictly decreasing, so no peaks exist.

## Constraints

- 1 <= len(readings) <= 1000
- -10^6 <= readings[i] <= 10^6


## Complexity

**Time Complexity:** O(N)

**Space Complexity:** O(1)
