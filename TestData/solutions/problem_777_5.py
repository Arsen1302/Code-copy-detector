class Solution:
    def solution_777_5(self, grid: List[List[int]]) -> int:
        n = len(grid) # dimension
        
        ans = -1
        queue = [(i, j) for i in range(n) for j in range(n) if grid[i][j]]
        while queue: 
            newq = []
            for i, j in queue: 
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                    if 0 <= ii < n and 0 <= jj < n and not grid[ii][jj]: 
                        newq.append((ii, jj))
                        grid[ii][jj] = 1 # mark as visited 
            queue = newq
            ans += 1
        return ans or -1