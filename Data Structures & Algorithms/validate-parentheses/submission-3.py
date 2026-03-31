class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")":"(","]":"[","}":"{"}
        stack = []

        for c in s[::-1]:
            # if c is a closing bracket (and is therefore in the dict)
            if c in closeToOpen:
                stack.append(c)
            # if c is an open bracket (and is not in the dict)
            else:
                # check the dict for the last closing bracket added... 
                # ...is the corresponding open bracket?
                if len(stack) > 0 and closeToOpen[stack[-1]] == c:
                    stack.pop()
                else:
                    return False

        if len(stack) > 0: 
            return False
        return True