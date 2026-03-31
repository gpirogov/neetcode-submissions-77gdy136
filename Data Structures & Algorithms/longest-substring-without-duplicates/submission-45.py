class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        L = 0
        R = 1
        bestLength = 1
        seenChars = {s[0]: 0}

        while R < len(s):
            if s[R] in seenChars:
                temp = i = seenChars[s[R]] # get index of old found char
                while i > -1 and s[i] in seenChars:
                    if seenChars[s[i]] == i: 
                        seenChars.pop(s[i])
                    i -= 1
                L = temp + 1
            else:
                if R - L + 1 > bestLength: bestLength = R - L + 1
            seenChars[s[R]] = R # can combine with above! even though done for different purposes.
            R += 1

        return bestLength
            