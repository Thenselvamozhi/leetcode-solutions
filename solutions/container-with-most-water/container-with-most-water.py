class Solution(object):
    def maxArea(self, height):
        i, j = 0, len(height)-1
        maxWater = 0
        while i < j:
            minHeight = min(height[i], height[j])
            water = minHeight * (j - i)
            maxWater = max(maxWater, water)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxWater