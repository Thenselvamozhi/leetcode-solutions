class Solution:
    def findNthDigit(self, n: int) -> int:
        numberRange = 1
        while n > ((10**numberRange) - (10**(numberRange-1))) * numberRange:
            n -= ((10**numberRange) - (10**(numberRange-1))) * numberRange
            numberRange += 1
        digit = (10**(numberRange-1)) + ((n-1) // numberRange)
        index = n % numberRange
        return int(str(digit)[index-1])