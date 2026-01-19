class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        op = []
        for i in nums:
            index = abs(i)
            nums[index - 1] = -(abs(nums[index - 1]))
        for i in range(len(nums)):
            if nums[i] > 0:
                op.append(i+1)
        return op