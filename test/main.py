matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

def searchMatrix(matrix, target):
    if not matrix:
        return False
    row, columb = len(matrix), len(matrix[0])
    left, right = 0, row * columb - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_row, mid_col = divmod(mid, columb)
        
        if matrix[mid_row][mid_col] == target:
            return True
        elif matrix[mid_row][mid_col] < target:
            left = mid - 1
        else:
            right = mid - 1
    return False
    

print(searchMatrix(matrix, target))
    
    

            

        