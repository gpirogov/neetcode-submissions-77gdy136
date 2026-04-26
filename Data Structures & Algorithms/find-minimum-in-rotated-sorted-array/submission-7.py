# BASICALLY A COMPLETE RE-DO TBH (AFTER 20 MINUTES). OPTIMAL IS CLOSE TO KOKO LOGIC ACTUALLY!
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1

        while L <= R: 
            M = (L+R)//2
            if nums[M] < nums[R]:
                R = M
            elif nums[M] > nums[R]:
                #if L == M: return nums[R]
                L = M+1
            else:
                return nums[M]