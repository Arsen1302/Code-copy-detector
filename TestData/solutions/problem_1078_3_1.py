class Solution:
    def solution_1078_3_1(self, grid: List[List[int]]) -> int:
        def solution_1078_3_2(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        
        @lru_cache(None)
        def solution_1078_3_3(row,col,product):
            if not solution_1078_3_2(row, col):
                    return -1
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return product * grid[row][col]
            return max(solution_1078_3_3(row+1,col, product * grid[row][col]),solution_1078_3_3(row,col+1, product * grid[row][col]))           
        max_product = solution_1078_3_3(0,0,1)
        return max_product %(10**9+7) if max_product!=-1 else -1