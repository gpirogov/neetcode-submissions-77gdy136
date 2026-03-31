class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        daysUntilWarmer = [0] * len(temperatures)
              
        i = len(temperatures)-1
        stack = [i] 

        while i >= 0:
            while len(stack):
                if temperatures[stack[-1]] > temperatures[i]:
                    daysUntilWarmer[i] = stack[-1]-i
                    stack.append(i)
                    break
                else:
                    stack.pop()

            if not len(stack):
                stack.append(i)
                
            i-= 1

        return daysUntilWarmer