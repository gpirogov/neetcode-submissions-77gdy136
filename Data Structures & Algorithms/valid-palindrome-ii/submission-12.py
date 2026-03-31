class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        startIndex = 0
        endIndex = len(s)-1

        while startIndex < endIndex:
            if s[startIndex] == s[endIndex]:
                startIndex += 1
                endIndex -= 1
            else: 
                if s[startIndex+1:endIndex+1] == s[startIndex+1:endIndex+1][::-1]:
                    return True
                elif s[startIndex:endIndex-1+1] == s[startIndex:endIndex-1+1][::-1]:
                    return True
                else:
                    return False
        return True