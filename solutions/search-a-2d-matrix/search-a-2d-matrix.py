class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        k = 0
        n = len(matrix)
        m = len(matrix[0])
        temp = [0] * (m*n)
        for i in range(n):
            for j in range(m):
                temp[k] = matrix[i][j]
                k+=1
        
        l, h = 0, k-1
        while (l <= h):
            mid = (l + h) // 2
            if temp[mid] == target:
                return True
            elif temp[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return False