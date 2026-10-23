class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = 0
        for index, letter in enumerate(s):
            revIndex = 26 - (ord(letter) - ord('a'))
            degree += (index + 1) * revIndex
        return degree