class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sort order: 0, 1, 2

        colorCount = {0 : 0, 1 : 0, 2 : 0}

        for i in nums:
            colorCount[i] += 1

        nums.clear()
        nums.extend([0] * colorCount[0])
        nums.extend([1] * colorCount[1])
        nums.extend([2] * colorCount[2])

        return