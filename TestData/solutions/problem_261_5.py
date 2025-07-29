class Solution:
    def solution_261_5(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        bal = 0
        # Expand grid
        grid.insert(0, [0]*cols)
        grid.append([0]*cols)
        for i in range(rows+2):
            grid[i].append(0)
            grid[i].insert(0, 0)

        for i in range(1,rows+1):
            for j in range(1,cols+1):
                val = grid[i][j]
                # By symmetry, look down and right:
                if val: bal += 4*val-2*grid[i+1][j]-2*grid[i][j+1]

        return bal