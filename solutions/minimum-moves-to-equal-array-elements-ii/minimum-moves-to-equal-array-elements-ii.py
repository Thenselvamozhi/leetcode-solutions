class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        mid = n//2
        median = (nums[mid-1] + nums[mid]) // 2 if n % 2 == 0 else nums[mid]
        steps = 0
        for num in nums:
            steps += abs(median - num)
        return steps