class Solution:
    def f(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (self.f(n-1) + self.f(n-2))
    def fib(self, n: int) -> int:
        return self.f(n)