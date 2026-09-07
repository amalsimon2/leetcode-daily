# Explanation

The algorithm first finds the minimum and maximum values in the input array. It then uses a set for O(1) lookups to check every integer strictly between the minimum and maximum bounds. Any integer not found in the set is appended to the result list in ascending order.

## Time Complexity

O(N + D) where N is the number of elements in the array and D is the difference between the maximum and minimum values.

## Space Complexity

O(N + D) to store the set of unique elements and the resulting missing elements.
