class Solution:
    def f(self, x, n):    
        if n == 0:
            return 1.0
        half = self.f(x, n//2)
        if n % 2 == 0:
            return half * half
        return x * half * half

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.f(x, -n)
        return self.f(x, n)