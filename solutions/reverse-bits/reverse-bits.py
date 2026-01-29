class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n & 0xFFFFFFFF)[2:].zfill(32)
        rev_b = b[::-1]
        return int(rev_b, 2)