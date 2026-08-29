def solve(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right and arr[left] == target:
        left += 1
        
    while left <= right and arr[right] == target:
        right -= 1
        
    return max(0, right - left + 1)
