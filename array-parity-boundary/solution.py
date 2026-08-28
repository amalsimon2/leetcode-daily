def solve(nums):
    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 != 0]
    nums[:] = evens + odds
    return nums
