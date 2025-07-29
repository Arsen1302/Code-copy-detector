class Solution:
    def solution_1515_3(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        grid, artifact_id = [[-1] * n for _ in range(n)], 0 # Making the grid
        for r1, c1, r2, c2 in artifacts: # Populate the grid matrix
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    grid[r][c] = artifact_id
            artifact_id += 1
        for r, c in dig: # Change the grid row, col to -1 by traversing dig array.
            if grid[r][c] >= 0:
                grid[r][c] = -1
        artifacts_remaining = set() 
        for r in range(n):
            for c in range(n):
                if grid[r][c] >= 0: # > 0 means that there still remains an artifact underneath, thus add it to the array
                    artifacts_remaining.add(grid[r][c])
        return artifact_id - len(artifacts_remaining)