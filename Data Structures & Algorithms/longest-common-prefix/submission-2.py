class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lCP = ""
        stopHere = False

        # option 1 = start from beginning, work up
        # option 2 (optimization -- will do next) = start from shortest string and work backwards

        shortestStringInList = min(strs,key=len)

        for i in range(len(shortestStringInList)):
            prefixToCheck = shortestStringInList[0:i+1]

            prevLCP = lCP
            lCP = prefixToCheck
            for s in strs:
                if not s.startswith(prefixToCheck):
                    stopHere = True
                    break
            if stopHere:
                lCP = prevLCP
                break
        return lCP