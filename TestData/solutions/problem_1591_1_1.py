class Solution:
    def solution_1591_1_1(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        max_row, max_col = len(grid), len(grid[0])
        dp = [[-1] * max_col for _ in range(max_row)] 

        def solution_1591_1_2(row, col):
            if row == max_row - 1: # If last row then return nodes value
                return grid[row][col]
            if dp[row][col] == -1: # If DP for this node is not computed then we will do so now.
                current = grid[row][col] # Current Node Value
                res = float('inf') # To store best path from Current Node
                for c in range(max_col): # Traverse all path from Current Node
                    val = moveCost[current][c] + solution_1591_1_2(row + 1, c) # Move cost + Target Node Value
                    res = min(res, val)
                dp[row][col] = res + current # DP[current node] = Best Path + Target Node Val + Current Node Val
            return dp[row][col]

        for c in range(max_col):
            solution_1591_1_2(0, c) # Start solution_1591_1_2 from all nodes in 1st row
        return min(dp[0]) # Return min value from 1st row