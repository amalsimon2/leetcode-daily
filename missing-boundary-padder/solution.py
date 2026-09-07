def solve(nums):
    if not nums:
        return []
    
    min_val = min(nums)
    max_val = max(nums)
    
    present = set(nums)
    missing = []
    
    for i in range(min_val + 1, max_val):
        if i not in present:
            missing.append(i)
            
    return missing
