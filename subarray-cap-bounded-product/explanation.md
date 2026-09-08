# Explanation

We iterate through the array maintaining a streak of consecutive elements that are less than or equal to the cap. When we encounter an element <= cap, our streak increases by 1, and we add the new streak length to our total count, because a streak of length k contributes k new valid subarrays ending at the current index. When an element exceeds the cap, the streak is reset to 0.

## Time Complexity

O(N)

## Space Complexity

O(1)
