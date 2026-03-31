class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        anagramChkDict = dict()
        for i in range(len(s)):
            letterQty = anagramChkDict.get(s[i])
            if letterQty == None: letterQty = 0
            anagramChkDict[s[i]] = letterQty+1
        for x in t:
            if anagramChkDict.get(x) == None: return False
            if anagramChkDict[x] != t.count(x):
                return False
        return True

        # mhm, upon further reflection, a for loop that goes thru both, then direct comparison of dictS and dictT is faster. cool!