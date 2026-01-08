class Solution:

    def f(self, i, j, s, t, dp):
        if i<0 or j<0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if s[i] == t[j]:
            return 1 + self.f(i-1, j-1, s, t, dp)
        left = self.f(i-1, j, s, t, dp)
        right = self.f(i, j-1, s, t, dp)

        dp[i][j] = max(left, right)
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1]*n for _ in range(m)]
        ans = self.f(m-1, n-1, text1, text2, dp)
        return ans        