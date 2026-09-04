# Explanation

The algorithm initializes an empty result list and a pointer at the given start index. It then enters a while loop that continues as long as the pointer is within the bounds of the array. Inside the loop, it appends the element at the current pointer position to the result list and increments the pointer by the specified stride. Once the pointer exceeds or equals the array length, the loop terminates and the result list is returned.

## Time Complexity

O(N / stride) where N is the length of the array

## Space Complexity

O(N / stride) to store the collected elements
