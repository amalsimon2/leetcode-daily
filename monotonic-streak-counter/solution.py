def solve(nums):
    if not nums:
        return 0
    
    max_len = 1
    inc_len = 1
    dec_len = 1
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            inc_len += 1
            dec_len = 1
        elif nums[i] < nums[i - 1]:
            dec_len += 1
            inc_len = 1
        else:
            inc_len = 1
            dec_len = 1
        
        current_max = max(inc_len, dec_len)
        if current_max > max_len:
            max_len = current_max
            
    return max_len
