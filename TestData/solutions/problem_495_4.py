class Solution:
#     O(r, c) || O(r,c)
# Runtime: 90ms 76.16% memory: 13.9mb 53.23%
    def solution_495_4(self, grid: List[List[int]]) -> int:
        maxRowVal = [0] * len(grid[0])
        maxColVal = [0] * len(grid[0])
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                maxRowVal[row] = max(maxRowVal[row], grid[row][col])
                maxColVal[col] = max(maxColVal[col], grid[row][col])
                
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                result += min(maxRowVal[row], maxColVal[col]) - grid[row][col]
                
        return result