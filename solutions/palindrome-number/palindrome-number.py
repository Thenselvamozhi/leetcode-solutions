class Solution(object):
    def isPalindrome(self, x):
        rev = 0
        num = abs(x)         
        while num > 0:
            rev = (rev * 10) + (num % 10)
            num = num // 10
        if rev == x:
            return True
        else:
            return False