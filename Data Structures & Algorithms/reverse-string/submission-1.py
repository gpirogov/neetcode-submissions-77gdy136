import math
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        letterSlot = ''
        for i in range(math.floor(len(s)/2)):
            if s[i] != s[len(s)-1-i]:
                letterSlot = s[i]
                s[i] = s[len(s)-1-i]
                s[len(s)-1-i] = letterSlot

