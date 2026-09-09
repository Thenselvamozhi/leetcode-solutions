class Solution(object):
    def transpose(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        result = [[0]* n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = matrix[j][i]
        return result