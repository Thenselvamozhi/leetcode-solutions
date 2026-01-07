class Solution:
    def pivotInteger(self, n: int) -> int:
        s1 = 0
        tot_sum = (n*(n+1))//2
        for i in range(1, n+1):
            s1 = (i*(i+1))//2
            s2 = tot_sum - s1 + i
            if s1 == s2:
                return i
        return -1