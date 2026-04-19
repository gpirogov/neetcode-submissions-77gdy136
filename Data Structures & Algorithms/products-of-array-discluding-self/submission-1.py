class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # sol'n 1: two-pass.
        # 8m least optimal (actually incorrect) sol'n

        totalSum = 1
        result = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    result[i] = result[i] * nums[j]

    
        '''for i in nums:
            totalSum = totalSum * i

        for i, j in enumerate(nums):
            result[i] = 0 if j == 0 else totalSum // j'''

        return result