# Explanation

We use a two-pointer approach. A write_pointer keeps track of where the next non-zero element should be placed. As we iterate through the array with a read pointer, whenever we encounter a non-zero element, we copy it to the write_pointer index and increment write_pointer. After processing all elements, we fill the remaining positions in the array with zeros.

## Time Complexity

O(N) where N is the length of the array

## Space Complexity

O(1) as the modification is done in-place
