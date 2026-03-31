# so the main lesson from this exercise is that you can't just set index of a newly initiated (empty) list to some value, right? like ans[2] = blah, when ans = [] (blank)? 

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''ans = nums.copy()
        ans.extend(nums)'''
        return nums + nums