class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]+1
        sum = 0
        next = nums[0]
        for i in nums:
            if i == next:
                sum += i
                next = i+1
            else:
                break
        while sum in nums:
            sum += 1
        return sum