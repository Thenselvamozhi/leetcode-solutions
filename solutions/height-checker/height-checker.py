class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        count, n = 0, len(heights)
        for i in range(n):
            if heights[i] != expected[i]:
                count += 1
        return count