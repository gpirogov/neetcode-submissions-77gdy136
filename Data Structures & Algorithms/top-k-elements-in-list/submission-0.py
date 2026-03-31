class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freqsAndNumsNoDupes = list(list())
        output = []
        # dFreq = {} # if duplicate vals in nums are always sequential, could track highestFreq + # vals away -- maybe not tho 
        for i in nums:
            if i not in d: 
                d[i] = 1
                freqsAndNumsNoDupes.append([-1,i])
            else: 
                d[i] += 1


        for j in freqsAndNumsNoDupes:
            j[0] = d[j[1]]
            #print(j)

        freqsAndNumsNoDupes.sort()
        
        for j in freqsAndNumsNoDupes[::-1]: # should stop when have done k elements.
            output.append(j[1])
            #print(j)

        return output[0:k]