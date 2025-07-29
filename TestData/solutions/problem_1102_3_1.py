class Solution:
    def solution_1102_3_1(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        
        def solution_1102_3_2(x): 
            """Return True if given effort is enough."""
            stack = [(0, 0)] # i|j|h starting from top-left 
            seen = set()
            while stack: 
                i, j = stack.pop()
                seen.add((i, j))
                if i == m-1 and j == n-1: return True # reaching bottom-right 
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in seen and abs(heights[ii][jj] - heights[i][j]) <= x: 
                        stack.append((ii, jj))
            return False 
            
        lo, hi = 0, 10**6
        while lo < hi: 
            mid = lo + hi >> 1
            if not solution_1102_3_2(mid): lo = mid + 1
            else: hi = mid
        return lo