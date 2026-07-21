class Solution:
    def isHappy(self, n: int) -> bool:
        if (n==1 or n==7):
            return True
        if (n<10):
            return False
        else:
            sum = 0
            while(n > 0):
                a = n % 10
                sum += a*a
                n = n // 10
            return self.isHappy(sum)