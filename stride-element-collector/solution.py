def solve(arr, start, stride):
    result = []
    curr = start
    while curr < len(arr):
        result.append(arr[curr])
        curr += stride
    return result
