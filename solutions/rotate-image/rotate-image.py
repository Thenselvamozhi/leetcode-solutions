class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(m)):
            for j in range(i+1, len(m)):
                m[i][j], m[j][i] = m[j][i], m[i][j]
        
        for i in range(len(m)):
            l, h = 0, len(m)-1
            while (l < h):
                m[i][l], m[i][h] = m[i][h], m[i][l]
                l += 1
                h -= 1