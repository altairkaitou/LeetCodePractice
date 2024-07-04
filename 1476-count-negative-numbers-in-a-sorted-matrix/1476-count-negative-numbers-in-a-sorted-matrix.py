class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        left = 0
        count = 0
        n = len(grid)
        
        right = len(grid[0]) - 1

        while right >= 0 and left < n:
            if grid[left][right] < 0:
                count += n - left
                right -= 1
            else:
                left += 1
        
        return count

        