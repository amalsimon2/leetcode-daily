def solve(nums):
    pos = [x for x in nums if x > 0]
    neg = [x for x in nums if x < 0]
    
    result = []
    p_idx = 0
    n_idx = 0
    
    start_with_pos = nums[0] > 0
    
    for i in range(len(nums)):
        if (i % 2 == 0) == start_with_pos:
            result.append(pos[p_idx])
            p_idx += 1
        else:
            result.append(neg[n_idx])
            n_idx += 1
            
    return result
