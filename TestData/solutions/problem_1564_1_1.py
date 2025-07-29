class Solution:
    def solution_1564_1_1(self, grid: List[List[str]]) -> bool:  
        m = len(grid)
        n = len(grid[0])
        @lru_cache(maxsize=None)
        def solution_1564_1_2(x, y, cnt):
            # cnt variable would act as a counter to track 
            # the balance of parantheses sequence
            if x == m or y == n or cnt < 0:
                return False
            
            # logic to check the balance of sequence
            cnt += 1 if grid[x][y] == '(' else -1
            
            # if balanced and end of grid, return True
            if x == m - 1 and y == n - 1 and not cnt:
                return True
            
            return solution_1564_1_2(x + 1, y, cnt) or solution_1564_1_2(x, y + 1, cnt)

        return solution_1564_1_2(0, 0, 0)