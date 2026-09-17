class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum, minLen, i, j = 0, len(nums)+1, 0, 0
        for j in range(len(nums)):
            currentSum += nums[j]
            while currentSum >= target:
                minLen = min(minLen, j-i+1)
                currentSum -= nums[i]
                i += 1
        return 0 if minLen == len(nums)+1 else minLen