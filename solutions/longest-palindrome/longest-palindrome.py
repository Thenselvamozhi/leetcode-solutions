class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        count = 0
        flag = 0
        for i in d:
            if d[i] % 2 == 0:
                count += d[i]
            else:
                count += d[i] - 1
                flag = 1
        if flag == 1:
            count += 1
        return count