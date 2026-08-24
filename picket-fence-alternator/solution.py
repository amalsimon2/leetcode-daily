def solve(nums):
    if len(nums) < 2:
        return True
    
    def get_sign(val):
        if val > 0:
            return 1
        elif val < 0:
            return -1
        return 0
    
    first_diff = nums[1] - nums[0]
    prev_sign = get_sign(first_diff)
    
    if prev_sign == 0:
        return False
        
    for i in range(2, len(nums)):
        diff = nums[i] - nums[i - 1]
        curr_sign = get_sign(diff)
        
        if curr_sign == 0 or curr_sign == prev_sign:
            return False
            
        prev_sign = curr_sign
        
    return True
