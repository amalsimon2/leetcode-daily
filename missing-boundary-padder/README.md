# missing-boundary-padder

**Day:** 16

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers representing discrete sensor readings, identify the minimum and maximum values present in the array. Then, return a new array containing all integers strictly between the minimum and maximum values, in ascending order, that were missing from the original array.

## Examples

### Input

[4, 1, 7, 7, 3]

### Output

[2, 5, 6]

### Explanation

The minimum is 1 and the maximum is 7. The complete range between them is [1, 2, 3, 4, 5, 6, 7]. The numbers missing from the original array are 2, 5, and 6.

### Input

[10, 10]

### Output

[]

### Explanation

The minimum and maximum are both 10. There are no integers strictly between them, so the result is empty.

## Constraints

- The input array will contain between 1 and 1000 integers.
- Array elements will be between -10000 and 10000.


## Complexity

**Time Complexity:** O(N + D) where N is the number of elements in the array and D is the difference between the maximum and minimum values.

**Space Complexity:** O(N + D) to store the set of unique elements and the resulting missing elements.
