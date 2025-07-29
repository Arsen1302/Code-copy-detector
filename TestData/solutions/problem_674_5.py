class Solution:
    def solution_674_5(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        visited = set()
        queue, new_queue = [], []
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # first find all initial rotten oranges
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        time = 0
        
        # bfs
        while queue:
            node = queue.pop(0)
            visited.add(node)
            
            for dir in dirs:
                new_row = node[0] + dir[0]
                new_col = node[1] + dir[1]
                if 0 <= new_row < row and 0 <= new_col < col and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    grid[new_row][new_col] = 2
                    visited.add((new_row, new_col))
                    new_queue.append((new_row, new_col))
            
            if len(queue) == 0 and len(new_queue) > 0:
                time += 1
                queue = new_queue
                new_queue = []
        
        # final check
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return time