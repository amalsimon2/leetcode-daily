def solve(nums, cap):
    total_subarrays = 0
    current_streak = 0
    for num in nums:
        if num <= cap:
            current_streak += 1
            total_subarrays += current_streak
        else:
            current_streak = 0
    return total_subarrays
