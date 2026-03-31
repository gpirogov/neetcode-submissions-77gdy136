class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word1Index = word2Index = 0

        newStr = ""

        while word1Index < len(word1) or word2Index < len(word2):
            if word1Index < len(word1): 
                newStr += word1[word1Index]
                word1Index += 1

            if word2Index < len(word2): 
                newStr += word2[word2Index]
                word2Index += 1

        return newStr