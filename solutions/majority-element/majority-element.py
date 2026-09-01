class Solution(object):
    def majorityElement(self, nums):
        current = nums[0]
        count = 0
        for i in nums:
            if i==current:
                count += 1
            else:
                count -= 1
                if count == 0:
                    current = i
                    count = 1
        return current