# PARTIAL I-THINK-OPTIMAL SOLUTION (AFTER 26 MINUTES)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1

        while L <= R: 
            M = (L+R)//2
            print(f"M = {M}")
            
            if nums[M] > nums[R]: #and M < L:
                if L == M: return nums[R]
                L = M
            elif nums[M] < nums[R]: #and M > L:
                R = M
            else:
                return nums[M]