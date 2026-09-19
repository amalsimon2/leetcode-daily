# Explanation

We iterate through the string tracking the current case type ('L' for lowercase, 'U' for uppercase) and the length of the current consecutive run. When the case changes or we reach the end of the string, we append the case and count to our result list and reset the counter.

## Time Complexity

O(N) where N is the length of the string.

## Space Complexity

O(N) to store the result string.
