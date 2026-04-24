class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # has duplicates.
        # "The first integer of every row is greater than the last integer of the previous row."

        # Part 1. traverse until get to right row.
        # MUST do so in log() time tho!
        #T, B = (0,0), (len(matrix)-1,len(matrix[len(matrix)-1])-1)
        T, B = 0, len(matrix)-1

        while T <= B:
            M = (T+B)//2
            if target > matrix[M][len(matrix[M])-1]:
                T = M+1
            elif target < matrix[M][0]:
                B = M-1
            else:
                # Part 2. simple binary search on chosen row
                L, R = 0, len(matrix[M])-1
                
                while L <= R:
                    M2 = (L+R)//2
                    if target < matrix[M][M2]:
                        R = M2-1
                    elif target > matrix[M][M2]:
                        L = M2+1
                    else:
                        return True
                return False
        return False