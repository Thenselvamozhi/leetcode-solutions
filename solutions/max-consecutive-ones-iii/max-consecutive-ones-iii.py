class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, maxi, zeros = 0, 0, 0
        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l+=1
            maxi = max(maxi, r-l+1)
        return maxi