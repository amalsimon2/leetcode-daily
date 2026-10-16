# Explanation

We can check every possible contiguous substring of the given string. For each starting index, we iterate through ending indices, keeping track of the counts of uppercase and lowercase letters. Whenever the counts are equal, we update our maximum length found so far.

## Time Complexity

O(N^2)

## Space Complexity

O(1)
