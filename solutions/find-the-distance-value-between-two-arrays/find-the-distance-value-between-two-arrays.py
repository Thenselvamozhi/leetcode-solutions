class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0
        for i in arr1:
            left, right = 0, len(arr2)
            while left < right:
                mid = (left + right) // 2
                if arr2[mid] >= i-d: #|arr1[i]-arr2[j]| <= d === i-d <= j <= i+d
                    right = mid
                else:
                    left = mid + 1
            if left == len(arr2) or arr2[left] > i+d:
                count += 1
        return count