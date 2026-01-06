class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l, maxi = 0, 0
        n = len(s)

        for r in range(n):
            if s[r] in d:
                if d[s[r]] >= l:
                    l = d[s[r]] + 1
                
            maxi = max(maxi, r-l+1)
            d[s[r]] = r
        
        return maxi