class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers) - 1
        i, j = 0, n
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return []