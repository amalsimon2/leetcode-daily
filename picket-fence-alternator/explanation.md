# Explanation

The algorithm computes the difference between adjacent elements sequentially. It extracts the sign of each difference (1 for positive, -1 for negative, and 0 for zero). If any difference is zero or has the same sign as the immediately preceding difference, the sequence fails the alternating condition and the function returns False. If all adjacent differences strictly alternate signs, it returns True.

## Time Complexity

O(n)

## Space Complexity

O(1)
