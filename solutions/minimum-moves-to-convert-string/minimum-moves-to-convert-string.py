class Solution:
    def minimumMoves(self, s: str) -> int:
        i = op = 0
        while i < len(s):
            if s[i] == 'X':
                op += 1
                i += 3
            else:
                i += 1
        return op