# picket-fence-alternator

**Day:** 5

**Difficulty:** Easy

**Category:** Arrays

## Problem

Given an array of integers, determine if the sequence of adjacent differences strictly alternates between strictly positive and strictly negative signs (or vice versa), which resembles the alternating heights of a picket fence.

## Examples

### Input

[1, 5, 2, 8, 3]

### Output

True

### Explanation

Differences are: 5-1=4 (+), 2-5=-3 (-), 8-2=6 (+), 3-8=-5 (-). The signs strictly alternate.

### Input

[1, 3, 2, 4]

### Output

True

### Explanation

Differences are: 3-1=2 (+), 2-3=-1 (-), 4-2=2 (+). The signs strictly alternate.

### Input

[1, 2, 3]

### Output

False

### Explanation

Differences are: 2-1=1 (+) and 3-2=1 (+). Both are positive, so they do not alternate.

## Constraints

- 2 <= nums.length <= 1000
- -10000 <= nums[i] <= 10000


## Complexity

**Time Complexity:** O(n)

**Space Complexity:** O(1)
