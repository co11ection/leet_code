n = 3
def generateMatrix(n):
    matrix = [[0] * n for i in range(n)]
    num = 1
    left, right, top, botton = 0, n - 1, 0, n - 1
    while num <= n*n:
        for index in range(left, right + 1):
            matrix[top][index] = num
            num += 1
        top += 1
        
        for index in range(top, botton + 1):
            matrix[index][right] = num
            num += 1
        right -= 1
        
        for index in range(right, left-1, -1):
            matrix[botton][index] = num
            num += 1
        botton -= 1
        
        for index in range(botton, top-1, -1):
            matrix[index][left] = num
            num += 1
        left += 1
    
    return matrix
    
gn = generateMatrix(5)

for row in gn:
    print(row)       