class Solution:
    def romanToInt(self, s: str) -> int:
        di = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = di[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if di[s[i]] < di[s[i+1]]:
                num -= di[s[i]]
            else:
                num += di[s[i]]
        return num