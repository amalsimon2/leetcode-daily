# Explanation

We iterate through each element of the array and check its neighbors. For the first element, we only compare it with the second element. For the last element, we only compare it with the second-to-last element. For any interior element, we check if it is strictly smaller than both its left and right neighbors. If it satisfies the condition, we increment our counter.

## Time Complexity

O(N)

## Space Complexity

O(1)
