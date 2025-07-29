class Solution:
    def solution_843_2(self, grid: List[List[int]]) -> int:
        
        # Time : O(N^2) 
        # Space : O(N)
        
        rows = len(grid)
        cols = len(grid[0])
        
        if cols == 1:
            return grid[0][0]
        
        dp = [float('inf') for i in range(cols + 2) ]
        min_in_left = [float('inf') if i in {0, cols +1} else 0 for i in range(cols + 2) ]
        min_in_right = [float('inf') if i in {0, cols +1} else 0 for i in range(cols + 2) ]
        
        for i in range(rows-1,-1,-1):
            for j in range(1,cols+1):
                dp[j] = grid[i][j-1] + min(min_in_left[j-1], min_in_right[j+1])
            
            for j in range(1, cols+1):
                min_in_left[j] = min(dp[j], min_in_left[j-1])
                
            for j in range(cols, 0, -1):
                min_in_right[j] = min(dp[j], min_in_right[j+1])
    
        return min(dp)