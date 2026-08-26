# Explanation

We iterate through the array starting from the second element (index 1) up to the second-to-last element (index n - 2). For each element, we check if it is strictly greater than its left and right neighbors. The first index that satisfies this condition is returned. If the loop completes without finding any such element, we return -1.

## Time Complexity

O(N)

## Space Complexity

O(1)
