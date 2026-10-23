class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s)-1
        newStr = list(s)
        def isLetter(letter):
            num = ord(letter)
            if ord('A') <= num <= ord('Z') or ord('a') <= num <= ord('z'):
                return True
            return False
        while left < right:
            if not isLetter(newStr[left]):
                left += 1
                continue
            if not isLetter(newStr[right]):
                right -= 1
                continue
            if isLetter(newStr[left]) and isLetter(newStr[right]):
                newStr[left], newStr[right] = newStr[right], newStr[left]
                left += 1
                right -= 1
        return ''.join(newStr)