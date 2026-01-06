class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        maxi = 0

        while (l < r):
            curr = min(height[l], height[r]) * (r-l)
            if curr > maxi:
                maxi = curr
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return maxi