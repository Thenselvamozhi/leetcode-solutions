class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = min(bloomDay)
        r = max(bloomDay)
        if len(bloomDay) < m*k:
            return -1
        while l <= r:
            mid = (l+r) // 2
            day = mid
            b, flowers = 0, 0
            for i in bloomDay:
                if day >= i:
                    flowers += 1
                    if flowers==k:
                        b+=1
                        flowers = 0
                else:
                    flowers = 0
            if b >= m:
                r = mid - 1
            else:
                l = mid + 1
        return l