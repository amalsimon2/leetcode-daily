from typing import List

def solve(nums: List[int]) -> List[int]:
    from collections import Counter
    counts = Counter(nums)
    unique_freqs = sorted(list(set(counts.values())))
    freq_to_rank = {freq: i + 1 for i, freq in enumerate(unique_freqs)}
    return [freq_to_rank[counts[num]] for num in nums]
