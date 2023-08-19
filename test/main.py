matrix = [[1,2],[2,2]]
def isTeoplistMatrix(matrix):
    rows = len(matrix)
    columbs = len(matrix[0])
    
    for i in range(rows):
        for j in range(columbs):
            if i > 0 and j > 0 and matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    return True


print(isTeoplistMatrix(matrix))
    
        
    