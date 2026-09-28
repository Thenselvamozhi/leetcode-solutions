class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        def canEat(piles, mid, h):
            hoursTaken = 0
            for i in piles:
                hoursTaken += math.ceil(i/mid)
            return True if hoursTaken <= h else False
        while left < right:
            mid = (left + right) // 2
            if canEat(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return left