class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        tot1 = ord(coordinate1[0]) - 96 + int(coordinate1[1])
        tot2 = ord(coordinate2[0]) - 96 + int(coordinate2[1])
        return True if (tot1 + tot2) % 2 == 0 else False