class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j, n = 0, len(s)
        for i in range(n):
            if s[i] == t[j]:
                j += 1
            if j == len(t):
                break
        return len(t) - j