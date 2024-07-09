class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count_neg = 0 
        rows = len(grid)
        cols = len(grid[0])
        row = 0  
        col = len(grid[0]) - 1

        while (row < rows and col >= 0):
            if grid[row][col] >= 0 :
                row += 1
            else:
                count_neg += rows - row
                col -= 1
        
        return count_neg
        



        