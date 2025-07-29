class Solution:
    def solution_515_4_1(self, grid: List[List[int]]) -> int:
        gsize = [0, 0]    # Size of each group, index start from 2
        cur = 2
        
        def solution_515_4_2(i, j, cur):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != 1: return
            gsize[cur] += 1
            grid[i][j] = cur
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]: 
                solution_515_4_2(i + di, j + dj, cur)
            
        todo = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):        
                if grid[i][j] == 0: todo.append((i, j))
                elif grid[i][j] == 1: 
                    gsize.append(0)
                    solution_515_4_2(i, j, cur)
                    cur += 1    # Move to the next group
                    
        if not todo: return gsize[2]    # Edge case: no zero in grid
        ans = 0
        for i, j in todo:
            visited = set()
            cur = 1
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and \
                    grid[i + di][j + dj] not in visited:
                    cur += gsize[grid[i + di][j + dj]]
                    visited.add(grid[i + di][j + dj])
            ans = max(ans, cur)
        
        return ans