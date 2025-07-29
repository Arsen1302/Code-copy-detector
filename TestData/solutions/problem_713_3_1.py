class Solution:
    def solution_713_3_1(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def solution_713_3_2(x,y):
            visited.add((x,y))
            for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
                if x+dx in (-1,m) or y+dy in (-1,n):
                    border.add((x, y))
                    continue
                if grid[x+dx][y+dy] != cc_color:
                    border.add((x, y))
                else: # neigh color same as cc_color
                    if (x+dx, y+dy) not in visited:
                        solution_713_3_2(x+dx, y+dy)
                        
        m, n = len(grid), len(grid[0])
        visited = set()
        border = set()
        cc_color = grid[row][col]
        solution_713_3_2(row, col)
        for i, j in border:
            grid[i][j] = color
        return grid