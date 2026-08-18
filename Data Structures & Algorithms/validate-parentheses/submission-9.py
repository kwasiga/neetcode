class Solution:
    def isValid(self, s: str) -> bool:
        res = { "}" : "{", "]" : "[", ")" : "(" }
        stack = []

        for c in s:
            if c in res:
                if stack and stack[-1] == res[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)

        return not stack



        