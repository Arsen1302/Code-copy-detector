class Solution:
    def solution_1564_5_1(self, grid: List[List[str]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        if grid[0][0] == ')' or (m + n - 1) % 2: return False
        
        @lru_cache(None)
        def solution_1564_5_2(x, y, ops):
			# if unpaired close bracket or remaining cannot match open brackets
            if ops < 0 or ops > (m + n - 1) // 2: return False
            if x == m - 1 and y == n - 1:
                return not ops
            
            for dx, dy in [(0, 1), (1, 0)]:
                nx, ny = x + dx, y + dy
                if not(0 <= nx < m and 0 <= ny < n): continue
                tmp = 1 if grid[nx][ny] == '(' else -1
                if solution_1564_5_2(nx, ny, ops + tmp):
                    return True
            return False
        
        
        return solution_1564_5_2(0, 0, 1)