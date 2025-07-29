class Solution:
    def solution_468_3(self, grid: List[List[int]]) -> int:
        n = len(grid) # dimension
        pq = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        while pq: 
            k, i, j = heappop(pq)
            if i == j == n-1: return k
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < n and 0 <= jj < n and (ii, jj) not in seen:
                    heappush(pq, (max(k, grid[ii][jj]), ii, jj))
                    seen.add((ii, jj))