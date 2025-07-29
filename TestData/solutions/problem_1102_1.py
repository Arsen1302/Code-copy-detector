class Solution:
    def solution_1102_1(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        
        queue = {(0, 0): 0} # (0, 0) maximum height so far 
        seen = {(0, 0): 0} # (i, j) -> heights 
        ans = inf 
        
        while queue: 
            newq = {} # new dictionary 
            for (i, j), h in queue.items(): 
                if i == m-1 and j == n-1: ans = min(ans, h)
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n: 
                        hh = max(h, abs(heights[i][j] - heights[ii][jj]))
                        if hh < seen.get((ii, jj), inf): 
                            seen[(ii, jj)] = hh 
                            newq[(ii, jj)] = hh
            queue = newq 
        return ans