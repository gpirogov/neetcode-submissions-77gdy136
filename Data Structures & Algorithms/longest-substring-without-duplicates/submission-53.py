class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        seenChars = {}
        bestLength = 0

        for R in range(len(s)):
            if s[R] in seenChars:
                # Move L to the right of the duplicate
                L = max(L, seenChars[s[R]] + 1)
            
            seenChars[s[R]] = R
            bestLength = max(bestLength, R - L + 1)
        
        return bestLength