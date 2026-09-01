class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, a in enumerate(nums):
            needed = target - a
            if needed in seen:
                return [seen[needed], i]
            seen[a] = i
