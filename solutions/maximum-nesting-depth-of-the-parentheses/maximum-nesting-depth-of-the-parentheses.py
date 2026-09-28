class Solution:
    def maxDepth(self, s: str) -> int:
        depth = r = 0
        for ch in s:
            if ch == ')':
                depth -= 1
            elif ch == '(':
                depth += 1
            r = max(r, depth)
        return r