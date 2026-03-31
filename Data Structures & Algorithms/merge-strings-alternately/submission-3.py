class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        wordIndex = 0

        newStr = []

        for i in range(max(len(word1),len(word2))):
            if wordIndex < len(word1): 
                newStr.append(word1[wordIndex])

            if wordIndex < len(word2): 
                newStr.append(word2[wordIndex])
                
            wordIndex += 1

        return "".join(newStr)