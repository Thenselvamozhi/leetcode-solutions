class Solution(object):
    def reverse(self, x):     
        rev = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while (x!=0):
            dig = x%10
            x //= 10
            rev = rev * 10 + dig
        rev*=sign
        return rev if 2**31 -1 >= rev >= -2**31 else 0