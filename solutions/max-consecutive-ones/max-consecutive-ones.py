class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxCon = count = 0
        for num in nums:
            if num == 1:
                count += 1
                maxCon = max(maxCon, count)
            else:
                count = 0
        return maxCon