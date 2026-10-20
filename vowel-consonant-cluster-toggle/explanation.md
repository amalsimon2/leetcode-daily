# Explanation

The algorithm iterates through the string to group contiguous blocks of characters that share the same vowel/consonant property. For each block, if the length of the block is even, its characters are converted to uppercase. If the length is odd, they remain lowercase. Finally, all modified blocks are concatenated back into a single string.

## Time Complexity

O(N) where N is the length of the string

## Space Complexity

O(N) to store the runs and the resulting string
