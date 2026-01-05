class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {}
        count = 0
        for i in stones:
            d[i] = d.get(i,0) + 1
        for j in jewels:
            if j in d:
                count += d[j]
        return count