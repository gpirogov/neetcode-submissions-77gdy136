class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # initial idea: just count number of each element. Can use dictionary
        #     ^ at each stage, can check if count > len / 2, stop if yes
        d = {}

        for i in range(len(nums)):
            if d.get(nums[i]) == None: d[nums[i]] = 0
            d[nums[i]] += 1
            if d[nums[i]] > (len(nums) / 2): return nums[i]