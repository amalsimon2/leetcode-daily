# Explanation

The algorithm separates the elements into two lists: one containing all the even numbers and another containing all the odd numbers. Because list comprehensions iterate through the array in order, the relative order of elements within each parity group is naturally preserved. Finally, the slices assignment updates the original array in-place and returns it.

## Time Complexity

O(N) where N is the length of the array

## Space Complexity

O(N) to store the separated even and odd sublists
