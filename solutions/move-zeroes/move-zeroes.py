class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        n = len(nums)

        for j in range(1, n):
            if nums[i] != 0:
                i += 1
            elif nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], 0
                i += 1