class Solution:
    def solution_640_4_1(self, grid: List[str]) -> int:        
        n, n3 = len(grid), len(grid) * 3
        mat = [[0] * n3 for _ in range(n3)]
        for i in range(n): 
            for j in range(n):
                if grid[i][j] == "/":
                    mat[i * 3][j * 3 + 2] = 1;
                    mat[i * 3 + 1][j * 3 + 1] = 1;
                    mat[i * 3 + 2][j * 3] = 1;
                if grid[i][j] == "\\":
                    mat[i * 3][j * 3] = 1;
                    mat[i * 3 + 1][j * 3 + 1] = 1;
                    mat[i * 3 + 2][j * 3 + 2] = 1;
        
        def solution_640_4_2(grid: List[List[int]], count: int, x, y, n):
                if grid[x][y] != 0: return
                grid[x][y] = count
                if x + 1 < n : 
                    solution_640_4_2(grid, count, x + 1, y, n)
                if y + 1 < n: 
                    solution_640_4_2(grid, count, x, y + 1, n)
                if x - 1 >= 0: 
                    solution_640_4_2(grid, count, x - 1, y, n)
                if y - 1 >= 0: 
                    solution_640_4_2(grid, count, x, y - 1, n)
        
        count = 0
        for i in range(n3):
            for j in range(n3):
                if mat[i][j] == 0:
                    count += 1
                    solution_640_4_2(mat, count, i, j, n3)
        return count