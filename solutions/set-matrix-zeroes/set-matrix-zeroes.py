class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        arr1 = [0] * n
        arr2 = [0] * m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    arr1[i] = 1
                    arr2[j] = 1
        
        for i in range(n):
            if arr1[i] == 1:
                for j in range(m):
                    matrix[i][j] = 0
        
        for j in range(m):
            if arr2[j] == 1:
                for i in range(n):
                    matrix[i][j] = 0