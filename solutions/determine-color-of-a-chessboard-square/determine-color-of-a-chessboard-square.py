class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        charInt = ord(coordinates[0]) - 97 + 1
        tot = charInt + int(coordinates[1])
        return True if (tot % 2) == 1 else False