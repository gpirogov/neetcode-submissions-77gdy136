class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word1Index = word2Index = 0
        word1Done = word2Done = False

        newStr = ""

        while not word1Done or not word2Done:
            if not word1Done and word1Index < len(word1): 
                newStr += word1[word1Index]
                word1Index += 1
            else: word1Done = True

            if not word2Done and word2Index < len(word2): 
                newStr += word2[word2Index]
                word2Index += 1
            else: word2Done = True

        return newStr