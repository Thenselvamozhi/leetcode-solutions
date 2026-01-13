class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        max_length = 1
        
        if n == 1:
            return s
    
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
        
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j] and length > max_length:
                    start = i
                    max_length = length
        
        return s[start: start + max_length]