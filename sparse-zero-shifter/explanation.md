# Explanation

The algorithm uses a two-pointer approach. We maintain an index `non_zero_idx` that tracks where the next non-zero element should be placed. We iterate through the array, and whenever we encounter a non-zero element, we place it at `non_zero_idx` and increment the pointer. After processing all elements, the remaining positions from `non_zero_idx` to the end of the array are filled with zeros.

## Time Complexity

O(N) where N is the length of the array

## Space Complexity

O(1) as the transformation is done in-place
