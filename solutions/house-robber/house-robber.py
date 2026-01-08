class Solution:
    def f(self, i, arr, dp):
        if i == 0:
            dp[i] = arr[0]
            return dp[i]
        if i < 0:
            return 0
        if dp[i] != -1:
            return dp[i]
        not_pick = 0 + self.f(i-1, arr, dp)
        pick = arr[i] + self.f(i-2, arr, dp)
        dp[i] = max(not_pick, pick)
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        ans = self.f(n-1, nums, dp)
        return ans