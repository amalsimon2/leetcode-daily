# Explanation

We iterate through the array to identify contiguous identical segments (runs) of elements. For each run, we check its length against the threshold k. If the run length is at least k, we keep the elements; otherwise, we discard them. This requires a single pass over the array using a two-pointer approach for run detection.

## Time Complexity

O(N)

## Space Complexity

O(N)
