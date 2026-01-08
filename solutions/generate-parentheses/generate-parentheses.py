class Solution:
    def f(self, open, close, s, ans, n):
        if close == n and open == n:
            ans.append(s)
        if open < n:
            self.f(open+1, close, s+'(', ans, n)
        if close < n and close < open:
            self.f(open, close+1, s+')', ans, n)
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.f(0, 0, '', ans, n)
        return ans