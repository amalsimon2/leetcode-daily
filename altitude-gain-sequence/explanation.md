# Explanation

We can simulate the journey starting from altitude 0. We iterate through each altitude change in the array, maintain a running sum of the current altitude, and keep track of the highest altitude reached so far. Since the starting altitude is 0, the maximum altitude is initialized to 0 to handle cases where all net changes are negative.

## Time Complexity

O(n)

## Space Complexity

O(1)
