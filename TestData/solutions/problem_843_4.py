class Solution:
    def solution_843_4(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]

        if grid[0][0] <= grid[0][1]:
            prevMin1, prevMin2 = 0, 1
        else:
            prevMin1, prevMin2 = 1, 0
    
        for j in range(2, n):
            if grid[0][j] <= grid[0][prevMin1]:
                prevMin1, prevMin2 = j, prevMin1
            elif grid[0][j] < grid[0][prevMin2]:
                prevMin2 = j
        
        for i in range(1, n):
            min1, min2 = -1, -1
            min1Val = min2Val = math.inf
            
            for j in range(n):
                if j != prevMin1:
                    grid[i][j] += grid[i - 1][prevMin1]
                else:
                    grid[i][j] += grid[i - 1][prevMin2]
                
                if grid[i][j] <= min1Val:
                    min1, min2 = j, min1
                    min1Val, min2Val = grid[i][j], min1Val
                elif grid[i][j] < min2Val:
                    min2 = j
                    min2Val = grid[i][j]
                
            prevMin1, prevMin2 = min1, min2
        
        return min(grid[-1])