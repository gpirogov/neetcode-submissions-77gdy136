class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        daysUntilWarmer = [0] * len(temperatures)
        stack = []
        #numPops = 0
        

        i = len(temperatures)-1
        print("test")

        while i >= 0:
            #numPops = 0
            print(f"START (1): i = {i}, stack = {stack}, daysUntilWarmer = {daysUntilWarmer}")


            if not len(stack): # can we remove this? i added a new one below.
                stack.append(i)
                print(f"START (1.5): i = {i}, stack = {stack}, daysUntilWarmer = {daysUntilWarmer}")

            while len(stack):
                if temperatures[stack[-1]] > temperatures[i]:
                    daysUntilWarmer[i] = stack[-1]-i # ???
                    stack.append(i)
                    print(f"START (2a): i = {i}, stack = {stack}, daysUntilWarmer = {daysUntilWarmer}")
                    break
                else:
                    # recursively do this while loop.... --> checking if its any of the items in the stack
                    # ^ OOOOOR -- 

                    stack.pop()
                    #numPops += 1
                    print(f"START (2b): i = {i}, stack = {stack}, daysUntilWarmer = {daysUntilWarmer}")

            if not len(stack):
                stack.append(i)

            # if while loop ends w/o daysUntilWarmer[i] being set, can do nothing as daysUntilWarmer[i] is 0 by default
            print(f"END (x):   i = {i}, stack = {stack}, daysUntilWarmer = {daysUntilWarmer}")
            i-= 1

        # return: list(number of days between 1st, 2nd, 3rd, and next warmer day. else 0)
        return daysUntilWarmer