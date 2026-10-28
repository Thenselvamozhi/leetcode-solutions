# ==========================================================
# 1. Two Sum
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 1775 ms (Beats 11%)
# Memory     : 19.6 MB (Beats 98%)
# Link       : https://leetcode.com/problems/two-sum/
# ==========================================================

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]