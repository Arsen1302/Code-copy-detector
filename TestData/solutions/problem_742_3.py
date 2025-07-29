class Solution:
    def solution_742_3(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 0: 
            ans = 0 
            grid[0][0] = 1
            queue = deque([(0, 0)])
            while queue: 
                ans += 1
                for _ in range(len(queue)): 
                    i, j = queue.popleft()
                    if i == j == n-1: return ans
                    for ii in range(i-1, i+2): 
                        for jj in range(j-1, j+2): 
                            if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] == 0: 
                                grid[ii][jj] = 1
                                queue.append((ii, jj))
        return -1