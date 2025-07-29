class Solution:
    def solution_661_5_1(self, grid: List[List[int]]) -> int:
        row_movements = [1, -1, 0, 0] # Possible changes in row index
        col_movements = [0, 0, 1, -1] # Possible changes in row index
        ways = 0 # Answer variable
        max_row = len(grid)
        max_col = len(grid[0])
        total = max_row * max_col # Total number of blocks to cover
        for r in range(max_row):
            for c in range(max_col):
                if grid[r][c] == -1: # Remove the blocks which are obstacles
                    total -= 1

        def solution_661_5_2(row, col, visited, current_count): # Current row, col, visited indices and number of blocks traversed so far.
            nonlocal ways
            if grid[row][col] == 2 and current_count >= total: # Breaking conditions met
                ways += 1
				return
            for i in range(4): # 4 Possible movements from a certain row, column index
                r = row + row_movements[i]
                c = col + col_movements[i]
                if 0 <= r < max_row and 0 <= c < max_col and grid[r][c] != -1 and not visited[r][c]: # If the new r, c index is in range, is not an obstacle and is not yet visited
                    visited[r][c] = True # Traverse forward with visited set to true
                    solution_661_5_2(r, c, visited, current_count + 1) # DFS traversal
                    visited[r][c] = False # Backtrack by setting visited to false

        for r in range(max_row):
            for c in range(max_col):
                if grid[r][c] == 1: # Starting index found
                    visited = [[False] * max_col for _ in range(max_row)]
                    visited[r][c] = True # Set starting index to True
                    solution_661_5_2(r, c, visited, 1) # Start DFS from starting index
                    return ways
        return 0