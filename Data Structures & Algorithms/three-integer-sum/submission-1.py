class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Create list of lists that will be outputted
        sortedNums = sorted(nums)
        # print(sortedNums)
        allThreeSums = []
        # allThreeSumIndices = []




        i = 0
        j = 1
        k = 1
        doubleBreak = False
        # assess all possible combinations
        # exlude all those with repeating positions
        # ^ this is a for loop where each position we begin with is ahead by 1
        while True:
            k+=1

            # OOB Check (probs make its own separate function)
            if k > len(sortedNums)-1:
                j+=1
                k=j+1
            if j > len(sortedNums)-2:
                i+=1
                j=i+1
                k=j+1
            if i > len(sortedNums)-3:
                break


            #NOTE TO FUTURE SELF IF REVIEW: Woooow, okay. so yeah. duely noted -- not reading instructs carefully (avoid duplicate "indices" instead of "values"), i caused myself a lot of heartache and debugging.
            """
            while sortedNums[k] == sortedNums[i] or sortedNums[j] == sortedNums[i] or sortedNums[j] == sortedNums[k]:
                k+=1
                # OOB Check (probs make its own separate function)
                if k > len(sortedNums)-1:
                    j+=1
                    k=j+1
                if j > len(sortedNums)-2:
                    i+=1
                    j=i+1
                    k=j+1
                if i > len(sortedNums)-3:
                    doubleBreak = True
                    break
                # print("i = ",i,"j = ",j,"k = ",k)
            if doubleBreak: break
            

            # OOB Check (probs make its own separate function)
            if k > len(sortedNums)-1:
                j+=1
                k=j+1
            if j > len(sortedNums)-2:
                i+=1
                j=i+1
                k=j+1
            if i > len(sortedNums)-3:
                break
            """

            # include if sum == 0
            if sortedNums[i]+sortedNums[j]+sortedNums[k] == 0:
                if [sortedNums[i],sortedNums[j],sortedNums[k]] not in allThreeSums:
                    allThreeSums.append([sortedNums[i],sortedNums[j],sortedNums[k]])

                # allThreeSumIndices.append([i,j,k])
        # print(allThreeSumIndices)
        return allThreeSums
        