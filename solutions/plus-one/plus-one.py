class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        rem = (digits[n-1] + 1) // 10
        if rem == 0:
            digits[n-1] = digits[n-1] + 1
            return digits
        else:
            i = n-1
            while digits[i] == 9 and i > -1:
                i -= 1
            if i == -1:
                return [1] + [0]*n
            else:
                digits[i] = digits[i] + 1
                s = n - i - 1
                return digits[0:i+1] + [0] * s
