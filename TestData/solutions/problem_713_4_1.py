class Solution:
    def solution_713_4_1(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        R, C = len(grid), len(grid[0])
        orig_col = grid[row][col]
        s = set()
        border = set()
        if orig_col == color: return grid
        def solution_713_4_2(grid, sr, sc):
            if grid[sr][sc] == orig_col and (sr, sc) not in s:
                s.add((sr, sc))
                if sr>=1: solution_713_4_2(grid, sr-1, sc)
                if sr<=R-2: solution_713_4_2(grid, sr+1, sc)
                if sc>=1: solution_713_4_2(grid, sr, sc-1)
                if sc<=C-2: solution_713_4_2(grid, sr, sc+1)
                if sr==0 or sr==R-1 or sc==0 or sc==C-1:
                    border.add((sr,sc))
                elif grid[sr-1][sc]!= orig_col or grid[sr+1][sc]!= orig_col or grid[sr][sc-1]!= orig_col or grid[sr][sc+1]!= orig_col:
                    border.add((sr,sc))
                                    
                    
        solution_713_4_2(grid, row, col)
        for (sr,sc) in border:
            grid[sr][sc] = color
        return grid