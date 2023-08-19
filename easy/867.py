class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows = len(matrix)
        columbs = len(matrix[0])
    
        tr_matrix = [[0] * rows for i in range(columbs)]
    
        for i in range(rows):
            for j in range(columbs):
                tr_matrix[j][i] = matrix[i][j] 
            
        return tr_matrix