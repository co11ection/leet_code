matrix = [[1,2,3],[4,5,6],[7,8,9]]
def transpose(matrix):
    rows = len(matrix)
    columbs = len(matrix[0])
    
    transpose_matrix = [[0] * rows for i in range(columbs)]
    
    for i in range(rows):
        for j in range(columbs):
            transpose_matrix[j][i] = matrix[i][j] 
            
    return transpose_matrix

print(transpose(matrix))
