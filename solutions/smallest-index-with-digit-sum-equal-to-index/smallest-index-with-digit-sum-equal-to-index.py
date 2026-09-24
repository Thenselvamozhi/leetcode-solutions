class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num, tot = nums[i], 0
            while num > 0:
                rem = num % 10
                tot += rem
                num //= 10
            if tot == i:
                return i
        return -1