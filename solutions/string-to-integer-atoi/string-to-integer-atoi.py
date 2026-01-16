class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        sign = 1
        digit = "1234567890"
        n = len(s)
        result = 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        i = 0
        while i<n and s[i] == " ":
            i += 1
        if i == n:
            return 0

        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i+=1

        while i < n and s[i] in digit:
            dig = int(s[i])
            result = (result * 10) + dig
            i += 1
        
        if sign * result >= INT_MAX:
            return INT_MAX
        elif sign * result <= INT_MIN:
            return INT_MIN

        return result * sign