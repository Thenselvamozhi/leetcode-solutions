class Solution:
    def f(self, i, j, s, dp):
        if i==j:
            return 1
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if s[i]==s[j]:
            dp[i][j] = 2 + self.f(i+1, j-1, s, dp)
            return dp[i][j]
        left = self.f(i+1, j, s, dp)
        right = self.f(i, j-1, s, dp)
        dp[i][j] = max(left, right)
        return dp[i][j]
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1]*n for _ in range(n)]
        ans = self.f(0, n-1, s, dp)
        return ans