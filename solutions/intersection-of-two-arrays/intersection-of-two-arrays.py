class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set()
        ans = []
        for num in nums1:
            seen.add(num)
        for num in nums2:
            if num in seen:
                ans.append(num)
                seen.remove(num)
        return ans