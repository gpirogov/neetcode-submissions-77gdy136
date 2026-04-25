# PARTIAL I-THINK-OPTIMAL SOLUTION (AFTER 26 MINUTES)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        smallestVal = nums[0]
        rotation = 0

        # step 1: determine rotation via application of range based bin search
        smallestVal = min(nums) # temp
        rotation = 4 # temp
 
        
        # step 2: perform normal bin search, *mod*ified by rotation
        L, R = 0, len(nums)-1

        while L <= R: 
            '''
            LMod = (0 + rotation) % len(nums)
            RMod = (len(nums)-1 + rotation) %  len(nums)
            print(f"L = {L}, LMod = {LMod}, R = {R}, RMod = {RMod}")
            '''
            M = (L+R)//2
            MMod = (M + rotation) % len(nums)
            print(f"M = {M}, MMod = {MMod}")
            
            if smallestVal < nums[MMod]:
                R = M-1
            elif smallestVal > nums[MMod]:
                L = M+1
            else:
                return nums[MMod]

# FINAL NOTES BEFORE PAUSE THEN FINISH LATER:
# of course, we won't need step 2 actually if we find smallestVal in step 1.
# ^ what we're really looking for is .....