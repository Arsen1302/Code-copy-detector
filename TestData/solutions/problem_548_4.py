class Solution:
    def solution_548_4(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ones = [0] * cols
        
        # flip rows
        for r in range(rows):
            row = grid[r]
            flip = row[0] == 0
            
            for c in range(cols):
                if flip:
                    row[c] = 1 if row[c] == 0 else 0  # flip
                
                if row[c] == 1:
				    ones[c] += 1  # count number of 1s
                    
        half = rows / 2
        
        # flip cols
        for c in range(cols):
            if ones[c] >= half:
                continue
            
            for r in range(rows):
                grid[r][c] = 1 if grid[r][c] == 0 else 0  # flip
                
        # calculate
        res = 0
        for r in range(rows):
            for c in range(cols):
                res += grid[r][c] * 2 ** (cols - c - 1)
        
        return res