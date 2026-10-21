class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def isPossible(capacity):
            daysNeeded, load = 1, 0
            for weight in weights:
                if load + weight <= capacity:
                    load += weight
                else:
                    daysNeeded += 1
                    load = weight
            return daysNeeded <= days
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if isPossible(mid):
                right = mid
            else:
                left = mid + 1
        return left