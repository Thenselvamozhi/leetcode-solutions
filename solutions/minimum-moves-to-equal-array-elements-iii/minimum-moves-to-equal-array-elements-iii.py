class Solution:
    def minMoves(self, nums: List[int]) -> int:
        steps = 0
        maxNum = max(nums)
        for num in nums:
            steps += maxNum - num
        return steps