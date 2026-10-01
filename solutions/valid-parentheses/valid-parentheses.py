class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}
        for bracket in s:
            if bracket in ['(', '{', '[']:
                stack.append(bracket)
            elif stack != [] and pairs[bracket] == stack[-1]:
                stack.pop()
            else:
                return False
        if stack == []:
            return True
        return False