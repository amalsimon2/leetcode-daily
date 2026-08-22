def solve(arr):
    write_pointer = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[write_pointer] = arr[i]
            write_pointer += 1
    
    for i in range(write_pointer, len(arr)):
        arr[i] = 0
        
    return arr
