class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, maxi = 0, 0
        d = {}
        n = len(fruits)

        for r in range(n):
            d[fruits[r]] = d.get(fruits[r], 0) + 1
            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0: 
                    del d[fruits[l]]
                l += 1
            maxi = max(maxi, r-l+1)
        return maxi