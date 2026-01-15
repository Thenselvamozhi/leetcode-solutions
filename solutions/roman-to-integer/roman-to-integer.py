class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        prev = 0
        for i in s[::-1]:
            num = d[i]
            if num < prev:
                result -= num
            else:
                result += num
            prev = num
        return result