class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right, middle = [], [], []
        for i in nums:
            if i == pivot:
                middle.append(i)
            elif i > pivot:
                right.append(i)
            else:
                left.append(i)
        return left + middle + right