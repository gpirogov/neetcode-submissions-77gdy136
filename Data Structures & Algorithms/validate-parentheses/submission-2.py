class Solution:
    def isValid(self, s: str) -> bool:
        closedBraces = [")","]","}"]
        chars = list(s)

        stack = []

        # edge case
        if len(chars) == 1: return False

        while len(chars)!=0:

            # if stack is empty (can reformat to remove, to shorten code-legthe)
            if len(stack) == 0:
                if chars[len(chars)-1] not in closedBraces: return False
                stack.append(chars.pop())

            # if closed braces
            elif stack[len(stack)-1] in closedBraces:
                if chars[len(chars)-1] in closedBraces:
                    stack.append(chars.pop())
                elif stack[len(stack)-1] == ")" and chars[len(chars)-1] == "(" or stack[len(stack)-1] == "]" and chars[len(chars)-1] == "[" or stack[len(stack)-1] == "}" and chars[len(chars)-1] == "{":
                    chars.pop()
                    stack.pop()
                else:
                    return False

            # if open braces
            else:
                if stack[len(stack)-1] == "(" and chars[len(chars)-1] == ")" or stack[len(stack)-1] == "[" and chars[len(chars)-1] == "]" or stack[len(stack)-1] == "{" and chars[len(chars)-1] == "}":
                    chars.pop()
                    stack.pop()
                else:
                    return False
        
        #if has unclosed braces at the end
        if len(stack)!= 0: return False
        return True

        