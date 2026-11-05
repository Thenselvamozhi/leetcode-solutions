class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * len(nums)
        index = 0
        for i in range(n):
            ans[index] = nums[i]
            ans[index+1] = nums[i+n]
            index += 2
        return ans