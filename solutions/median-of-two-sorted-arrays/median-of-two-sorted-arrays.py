class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lis = []
        i, n = 0, len(nums1)
        j, m = 0, len(nums2)
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                lis.append(nums1[i])
                i += 1
            elif nums2[j] < nums1[i]:
                lis.append(nums2[j])
                j += 1
        if i < n:
            lis.extend(nums1[i:])
        if j < m:
            lis.extend(nums2[j:])
    
        length = len(lis)
        if length % 2 == 0:
            mid = length // 2
            median = (lis[mid] + lis[mid - 1]) / 2
        else:
            mid = length // 2
            median = lis[mid]
        return median