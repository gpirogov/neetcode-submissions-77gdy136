class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # sol'n 1: two-pass.

        totalSum = 1
        result = [0] * len(nums)

        for i in nums:
            totalSum = totalSum * i

        for i, j in enumerate(nums):
            result[i] = 0 if j == 0 else totalSum // j

        return result