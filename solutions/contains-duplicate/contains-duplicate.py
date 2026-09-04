class Solution(object):
    def containsDuplicate(self, nums):
        d = {}
        for n in nums:
            if n in d:
                return True
            else:
                d[n] = 1
        return False