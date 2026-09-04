# stride-element-collector

**Day:** 14

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers and a starting index along with a fixed positive stride, collect elements by repeatedly adding the stride to the current index until the index goes out of bounds of the array.

## Examples

### Input

arr = [10, 20, 30, 40, 50, 60], start = 1, stride = 2

### Output

[20, 40, 60]

### Explanation

Starting at index 1 (value 20), we take steps of size 2: indices 1, 3, and 5 correspond to values 20, 40, and 60.

### Input

arr = [5, 4, 3, 2, 1], start = 0, stride = 3

### Output

[5, 2]

### Explanation

Starting at index 0 (value 5), adding stride 3 gives index 3 (value 2). The next index 6 is out of bounds.

## Constraints

- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000
- 0 <= start < arr.length
- 1 <= stride <= 1000


## Complexity

**Time Complexity:** O(N / stride) where N is the length of the array

**Space Complexity:** O(N / stride) to store the collected elements
