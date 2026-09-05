class Solution(object):
    def isAnagram(self, s, t):
        d = {}
        if len(s) == len(t):
            for i in range(len(s)):
                d[s[i]] = d.get(s[i], 0) + 1
                d[t[i]] = d.get(t[i], 0) - 1
            if all(value == 0 for value in d.values()):
                return True
        return False