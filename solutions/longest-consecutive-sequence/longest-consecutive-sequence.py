class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        d = set()
        for num in nums:
            d.add(num)
        maxCount = 1
        for num in d:
            if num-1 not in d:
                current = num
                count = 1
                while current+1 in d:
                    count += 1
                    current += 1
                maxCount = max(maxCount, count)
        return maxCount