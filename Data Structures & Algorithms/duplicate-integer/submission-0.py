class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupCheckDict = dict()
        for x in nums :
            if dupCheckDict.get(x):
                return True
            else:
                dupCheckDict[x]=True
        return False