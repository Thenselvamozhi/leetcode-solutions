class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        p = n
        prime = [2, 3, 5]
        i = 0
        while (i <= 2):
            if (p % prime[i]) == 0:
                p /= prime[i]
            else:
                i += 1
        
        if p == 1:
            return True
        else:
            return False