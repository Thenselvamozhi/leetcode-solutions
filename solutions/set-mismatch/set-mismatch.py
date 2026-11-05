class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen = {}
        n = len(nums)
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
        missing = repeated = 0
        for i in range(1, n+1):
            if i not in seen:
                missing = i
            elif seen[i] == 2:
                repeated = i
            if missing and repeated:
                break
        return [repeated, missing]