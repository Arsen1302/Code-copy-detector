class Solution:
    def solution_1078_5(self, grid: List[List[int]]) -> int:
        numRows, numCols = len(grid), len(grid[0])
        maxProduct, minProduct = [[0] * numCols for _ in range(numRows)], [[0] * numCols for _ in range(numRows)]
        maxProduct[0][0], minProduct[0][0] = grid[0][0], grid[0][0]
        for row in range(1, numRows):
            minProduct[row][0] = minProduct[row - 1][0] * grid[row][0]
            maxProduct[row][0] = maxProduct[row - 1][0] * grid[row][0]
        for col in range(1, numCols):
            minProduct[0][col] = minProduct[0][col - 1] * grid[0][col]
            maxProduct[0][col] = maxProduct[0][col - 1] * grid[0][col]
        for row in range(1, numRows):
            for col in range(1, numCols):
                if grid[row][col] < 0:
                    maxProduct[row][col] = min(minProduct[row - 1][col], minProduct[row][col - 1]) * grid[row][col]
                    minProduct[row][col] = max(maxProduct[row - 1][col], maxProduct[row][col - 1]) * grid[row][col]
                else:
                    maxProduct[row][col] = max(maxProduct[row - 1][col], maxProduct[row][col - 1]) * grid[row][col]
                    minProduct[row][col] = min(minProduct[row - 1][col], minProduct[row][col - 1]) * grid[row][col]
        res = maxProduct[numRows - 1][numCols - 1]
        return res % 1000000007 if res >= 0 else -1