def solve(nums):
    current_altitude = 0
    max_altitude = 0
    for change in nums:
        current_altitude += change
        if current_altitude > max_altitude:
            max_altitude = current_altitude
    return max_altitude
