class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, count, curr_sum = 0, 0, 0
        n = len(nums)

        for r in range(n):
            curr_sum += nums[r]
            while curr_sum * (r-l+1) >= k:
                curr_sum -= nums[l]
                l += 1
            
            count += (r-l+1)
        
        return count