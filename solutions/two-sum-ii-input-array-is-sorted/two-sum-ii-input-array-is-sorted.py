class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1, 2]

        left, right = 0, len(numbers)-1

        while(left<right):
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum > target:
                right -= 1
            else:
                left += 1