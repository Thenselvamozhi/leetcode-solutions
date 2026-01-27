class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3

        for i in nums:
            count[i] += 1

        colour = 0
        index = 0
        while index < len(nums):
            for _ in range(count[colour]):
                nums[index] = colour
                index += 1
            colour += 1
            