class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(c+1):
            complement = c - (a*a)
            if complement < 0:
                break
            left, right = 0, c
            while left <= right:
                mid = (left + right) // 2
                square = mid * mid
                if square == complement:
                    return True
                elif square < complement:
                    left = mid + 1
                else:
                    right = mid - 1
        return False