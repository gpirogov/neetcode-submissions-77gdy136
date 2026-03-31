class Solution:
    def isValid(self, s: str) -> bool:
        closedBraces = [")","]","}"]
        chars = list(s)

        stack = []

        if len(chars) == 1: return False

        while len(chars)!=0:
            if len(stack) == 0:
                if chars[len(chars)-1] not in closedBraces: return False
                stack.append(chars.pop())
            elif stack[len(stack)-1] in closedBraces:
                if chars[len(chars)-1] in closedBraces:
                    stack.append(chars.pop())
                elif stack[len(stack)-1] == ")" and chars[len(chars)-1] == "(":
                    chars.pop()
                    stack.pop()
                elif stack[len(stack)-1] == "]" and chars[len(chars)-1] == "[":
                    chars.pop()
                    stack.pop()
                elif stack[len(stack)-1] == "}" and chars[len(chars)-1] == "{":
                    chars.pop()
                    stack.pop()
                else:
                    return False
            else:
                if stack[len(stack)-1] == "(" and chars[len(chars)-1] == ")":
                    chars.pop()
                    stack.pop()
                elif stack[len(stack)-1] == "[" and chars[len(chars)-1] == "]":
                    chars.pop()
                    stack.pop()
                elif stack[len(stack)-1] == "{" and chars[len(chars)-1] == "}":
                    chars.pop()
                    stack.pop()
                else:
                    return False
        if len(stack)!= 0: return False
        return True

        