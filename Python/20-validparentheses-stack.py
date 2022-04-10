class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict = {')':'(',']':'[','}':'{'}
        for i in s: 
            if i in ['(','[','{']: # opener bracket
                stack.append(i)
            else: 
                if len(stack) == 0: 
                    return False 
                elif bracket_dict[i] != stack[-1]:
                    return False
                else: 
                    stack.pop()
        if len(stack) != 0:
            return False
        return True