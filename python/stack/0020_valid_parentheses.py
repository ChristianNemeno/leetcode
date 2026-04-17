class Solution:
    def isValid(self, s: str) -> bool:

        close = { 
            ')' : '(',
            '}' : '{',
            ']' : '[',
         }
        stack = []

        for c in s:
            if c in close:
                #closed paren
                if stack and stack[-1] == close[c]:
                    stack.pop()
                else:
                    return False
            else:
                #means open just append 
                stack.append(c)

        return False if stack else True
        