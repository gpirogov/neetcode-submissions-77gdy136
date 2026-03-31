class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        L = 0
        R = 1
        bestLength = 1
        seenChars = {s[0]: 0}

        while R < len(s):
            if s[R] in seenChars:
                if R > 13: print(f"s[R] ({s[R]}, where R = {R}, i = {seenChars[s[R]]}) is in seenChars. bestLength = {bestLength}, seenChars = {seenChars}")
                temp = i = seenChars[s[R]] # get index of old found char
                while i > -1 and s[i] in seenChars: # for all
                    if seenChars[s[i]] == i: 
                        print(f"removing (s[i], i) ({s[i]}, {i}) from seenChars")
                        seenChars.pop(s[i])
                    i -= 1
                L = temp + 1
                seenChars[s[R]] = R
                # bestLength = max(bestLength, R - L)
            else:
                if R > 13: print(f"s[R] ({s[R]}, where R = {R}) is NOT in seenChars. bestLength = {bestLength}, seenChars = {seenChars}")
                if R - L + 1 > bestLength: bestLength = R - L + 1
                seenChars[s[R]] = R # can combine with above! even though done for different purposes.
            R += 1



        return bestLength
            