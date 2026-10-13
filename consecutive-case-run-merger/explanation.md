# Explanation

The algorithm iterates through the string while keeping track of the current case ('U' or 'L') and the length of the current consecutive run. Whenever the case of the character changes or the string ends, the accumulated run information (case letter and count) is appended to the result list, and the tracker resets for the new case. Finally, the list of run strings is joined together.

## Time Complexity

O(N) where N is the length of the string

## Space Complexity

O(N) to store the result runs
