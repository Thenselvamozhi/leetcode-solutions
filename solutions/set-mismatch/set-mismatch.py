class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s, d = len(nums)*(len(nums)+1)//2, set(nums)
        return [sum(nums)-sum(d), s-sum(d)]