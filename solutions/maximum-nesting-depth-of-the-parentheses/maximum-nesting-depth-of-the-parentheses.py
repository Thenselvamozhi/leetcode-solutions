class Solution(object):
    def maxDepth(self, s):
        depth = res = 0
        for ch in s:
            if ch == ')':
                depth -= 1
            elif ch == '(':
                depth += 1
            res = max(res, depth)
        return res