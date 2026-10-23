class Solution:
    def reverse(self, x: int) -> int:
        num, rev = abs(x), 0
        while num > 0:
            last = num % 10
            rev = (rev * 10) + last
            num //= 10
        if rev > (2**31)-1:
            rev = 0
        if x < 0:
            return -rev
        return rev