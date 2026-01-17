class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x, y = 0, n
        ans = [0] * len(nums)
        for i in range(0, len(nums), 2):
            ans[i] = nums[x]
            ans[i+1] = nums[y]
            x += 1
            y += 1
        return ans