class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return i+1 if nums[i] < target else i #i and j both end up with the same index