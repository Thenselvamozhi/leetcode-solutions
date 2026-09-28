class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        def canEat(piles, mid, h):
            hours = 0
            for i in piles:
                hours += math.ceil(i/mid)
            return True if hours <= h else False
        while left < right:
            mid = (left + right) // 2
            if canEat(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return left