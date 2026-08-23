# Explanation

We can use a frequency map (Counter) to count the occurrences of each sensor reading in the array. Then, we iterate through the unique readings, and for any reading that has a count of at least 2, we track the maximum value found. If no such reading exists, the default -1 is returned.

## Time Complexity

O(N) where N is the length of the readings array.

## Space Complexity

O(N) to store the frequency counts.
