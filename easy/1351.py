class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        row, columb = len(grid), len(grid[0])
        count = 0
        for index_i in range(row):
            for index_j in range(columb):
                if grid[index_i][index_j] < 0:
                    count+=1
                
        return count