class Solution:
    def solution_830_5(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
		# count number of servers in a row / col
        rows = defaultdict(int)
        cols = defaultdict(int)
        
        for r in range(M):
            for c in range(N):
                rows[r] += grid[r][c]
                cols[c] += grid[r][c]
                
        # not isolated if grid[r][c] == 1 and there's more than 1 server in same row or col
        notIsolated = lambda r, c: grid[r][c] and (rows[r] > 1 or cols[c] > 1)
        return sum(notIsolated(r, c) for r in range(M) for c in range(N))