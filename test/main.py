matrix = [[3,-7,8],[9,-11,13],[15,-16,17]]

def countNegative(self, grid):
    row, columb = len(grid), len(grid[0])
    count = 0
    for index_i in range(row):
        for index_j in range(columb):
            if grid[index_i][index_j] < 0:
                count+=1
                
    return count
s = 0
print(countNegative(s, matrix))
            
    
    

            

        