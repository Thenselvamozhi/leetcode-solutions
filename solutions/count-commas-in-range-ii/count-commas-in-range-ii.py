class Solution(object):
    def countCommas(self, n):
        count = 0
        power = 3
        while n > 0:
            n -= (10**power) - (10**(power-3))
            if n <= 0:
                break
            count += n
            power += 3
        return count