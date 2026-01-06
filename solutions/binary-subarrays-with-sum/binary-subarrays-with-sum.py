class Solution:
    def f(self, nums, k):
        l, total, s = 0, 0, 0
        n = len(nums)
        if k < 0:
            return 0
        for r in range(n):
            s += nums[r]
            while s > k:
                s -= nums[l]
                l += 1
            total += (r - l + 1)
        return total

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count1 = self.f(nums, goal)
        count2 = self.f(nums, goal-1)
        return count1 - count2