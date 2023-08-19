class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        rows = len(matrix)
        columbs = len(matrix[0])
    
        for i in range(rows):
            for j in range(columbs):
                if i > 0 and j > 0 and matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True
