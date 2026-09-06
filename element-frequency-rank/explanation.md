# Explanation

The algorithm first computes the frequency of each element using a frequency map (Counter). Then, it extracts all unique frequencies and sorts them in ascending order. A mapping from frequency to rank is constructed where the smallest frequency gets rank 1, the next gets rank 2, and so on. Finally, it constructs the result array by replacing each element with its corresponding frequency rank.

## Time Complexity

O(N log N)

## Space Complexity

O(N)
