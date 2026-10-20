class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res = []
        for index, nums in enumerate(nums):
            if nums == target:
                res.append(index)
            elif len(res) != 0:
                break
        return res