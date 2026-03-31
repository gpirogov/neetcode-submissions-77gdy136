import math
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        # loop thru the list, from start and end simultaneously
        for i in range(math.ceil(len(nums)/2)):
            # add both to (...)
            print(i)
            #NOTE TO FUTURE SELF IF REVIEW: originally I had:
            #  ((nums[i] + nums[len(nums)-i]) == target)  but if len(num) = 3 for instance num[3] = out of range!
            if ((nums[i] + nums[len(nums)-1-i]) == target) and (i != len(nums)-i):
                return [i,len(nums)-1-i]

            #NOTE TO FUTURE SELF IF REVIEW: originally I had:
            #if numsDict[nums[i]] != None:    but you can't check Dict()s like that.
            if numsDict.get(nums[i]) != None:
                return sorted([i,numsDict[nums[i]]])
            else:
                numsDict[target-nums[i]] = i

            if numsDict.get(nums[len(nums)-1-i]) != None:
                return sorted([len(nums)-1-i,numsDict[nums[len(nums)-1-i]]])
            else:
                numsDict[target-nums[len(nums)-1-i]] = len(nums)-1-i
        # if loop finishes with no numbers found, return Null
        return None