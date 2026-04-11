class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sort order: 0, 1, 2

        end = len(nums)-1
        mid = start = 0

        while mid <= end:
            if nums[mid] == 2:
                temp = nums[end]
                nums[end] = nums[mid]
                nums[mid] = temp
                #swap nums[mid] with nums[end]
                end-=1
            elif nums[mid] == 0:
                temp = nums[start]
                nums[start] = nums[mid]
                nums[mid] = temp
                # swap nums[mid] with nums[start]
                start += 1
            else: # if nums[mid] == 1
                mid += 1

            print(f"nums = {nums}, start = {start}, mid = {mid}, end {end}")
        return