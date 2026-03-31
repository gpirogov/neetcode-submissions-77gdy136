class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tempNums = []

        for i in range(len(nums)):
            '''print(i)'''
            if i == len(nums)-1 or nums[i] != nums[i+1]:
                '''print("Y")'''
                tempNums.append(nums[i])
            '''else:
                print("N")'''
        
        '''print(tempNums)'''
        nums[:] = tempNums
        return len(tempNums)