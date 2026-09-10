def solve(nums, k):
    if not nums:
        return []
    
    result = []
    n = len(nums)
    i = 0
    
    while i < n:
        j = i
        while j < n and nums[j] == nums[i]:
            j += 1
        
        run_length = j - i
        if run_length >= k:
            result.extend([nums[i]] * run_length)
        
        i = j
        
    return result
