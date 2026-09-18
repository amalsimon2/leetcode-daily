# Explanation

We iterate through the string to locate contiguous alphabetic clusters separated by non-alphabetic characters. For each cluster, we count uppercase and lowercase letters. If uppercase strictly outnumbers lowercase, we transform the cluster to uppercase; otherwise, we transform it to lowercase. Non-alphabetic characters are preserved in their original positions.

## Time Complexity

O(N) where N is the length of the string.

## Space Complexity

O(N) to store the resulting character list and final string.
