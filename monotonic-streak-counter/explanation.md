# Explanation

We iterate through the array while tracking the current length of strictly increasing and strictly decreasing streaks. If the sequence continues in either direction, we increment the respective streak length and reset the other. If elements are equal, both streaks reset to 1. Throughout the traversal, we keep track of the maximum streak length encountered.

## Time Complexity

O(N) where N is the length of the input array

## Space Complexity

O(1)
