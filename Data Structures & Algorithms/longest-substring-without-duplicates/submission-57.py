class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = R = bestLength = 0
        seenChars = {}

        for R in range(len(s)):
            if s[R] in seenChars:
                temp = i = seenChars[s[R]] # get index of old found char
                while i > -1 and s[i] in seenChars:
                    if seenChars[s[i]] == i: 
                        seenChars.pop(s[i])
                    i -= 1
                L = temp + 1
            if R - L + 1 > bestLength: bestLength = R - L + 1
            seenChars[s[R]] = R

        return bestLength