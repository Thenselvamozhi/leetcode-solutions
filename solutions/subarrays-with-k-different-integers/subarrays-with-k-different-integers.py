class Solution:
    def atmost(self, nums, k):
        d = {}
        l, count = 0, 0
        n = len(nums)
        for r in range(n):
            d[nums[r]] = d.get(nums[r], 0) + 1
            while len(d) > k:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l += 1
            count += (r-l+1)
        return count
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(nums, k) - self.atmost(nums, k-1)