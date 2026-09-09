def solve(nums: list[int], threshold: int) -> list[int]:
    return [x % threshold for x in nums]
