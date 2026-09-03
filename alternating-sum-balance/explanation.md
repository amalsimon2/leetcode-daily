# Explanation

The solution iterates through each possible index to remove from the array. For each removal, it calculates the alternating sum of the first half and the second half of the remaining array. If they match, the index is returned. If no index satisfies the condition, -1 is returned.

## Time Complexity

O(N^2)

## Space Complexity

O(N)
