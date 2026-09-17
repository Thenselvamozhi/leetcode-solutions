class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findTarget(nums, target, leftBias):
            left, right, result = 0, len(nums)-1, -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    if leftBias:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result
        return [findTarget(nums, target, True), findTarget(nums, target, False)]