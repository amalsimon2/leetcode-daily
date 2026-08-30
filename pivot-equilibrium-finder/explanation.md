# Explanation

We can solve this efficiently by first calculating the total sum of the array. Then, we iterate through the array while maintaining a running sum of elements to the left (left_sum). For any index i, the sum of elements to the right is simply (total_sum - left_sum - nums[i]). If left_sum equals the right sum, we return i immediately.

## Time Complexity

O(n)

## Space Complexity

O(1)
