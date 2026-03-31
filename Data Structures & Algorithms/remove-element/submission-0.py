class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # note: remove all val from nums IN PLACE

        originalLen = len(nums)
        valCount = 0

        # unclear: "It is not necessary to consider elements beyond the first k positions of the array."
        # will just attempt solution and if wrong, perhaps is because of this ^

        i = 0
        while i < originalLen - valCount:
            print(i)
            if nums[i] == val:
                nums.pop(i)
                valCount += 1
                i -= 1
            i += 1

        return originalLen - valCount