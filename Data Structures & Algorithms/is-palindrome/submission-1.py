class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerAlNumS = ''.join(c for c in s if c.isalnum()).lower()

        i = 0
        j = len(lowerAlNumS)-1
        while i <= j:
            if lowerAlNumS[i] != lowerAlNumS[j]:
                return False
            i += 1
            j -= 1


        return True