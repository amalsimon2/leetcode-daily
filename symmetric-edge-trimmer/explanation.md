# Explanation

We use a two-pointer approach. One pointer starts from the beginning (left) and advances as long as elements equal the target. The other pointer starts from the end (right) and moves backward as long as elements equal the target. We ensure that left does not cross right. The remaining length is the distance between the two pointers plus one, or zero if they cross.

## Time Complexity

O(N) where N is the length of the array

## Space Complexity

O(1)
