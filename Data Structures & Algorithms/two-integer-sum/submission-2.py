

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                j = seen[comp]
                return [j, i]  # j < i by construction
            seen[num] = i
        return None  # or raise an exception if you prefer