class Solution:
    def solution_1102_2(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0]) # dimensions 
        seen = {(0, 0): 0}
        pq = [(0, 0, 0)]
        while pq: 
            h, i, j = heappop(pq)
            if i == m-1 and j == n-1: return h
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n: 
                    hh = max(h, abs(heights[ii][jj] - heights[i][j]))
                    if (ii, jj) not in seen or hh < seen[ii, jj]: 
                        heappush(pq, (hh, ii, jj))
                        seen[ii, jj] = hh