class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # note: remove all val from nums IN PLACE

        # originalLen = len(nums)
        # valCount = 0

        # unclear: "It is not necessary to consider elements beyond the first k positions of the array."
        # will just attempt solution and if wrong, perhaps is because of this ^

        i = 0
        k = 0
        while i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            # k += 1
            i += 1

        return k