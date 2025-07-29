class Solution:
    def solution_163_4(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        indeg = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n): 
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n and matrix[i][j] < matrix[ii][jj]: 
                        indeg[ii][jj] += 1
        queue = deque([(i, j) for i in range(m) for j in range(n) if indeg[i][j] == 0])
        ans = 0
        while queue: 
            for _ in range(len(queue)): 
                i, j = queue.popleft()
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n and matrix[i][j] < matrix[ii][jj]: 
                        indeg[ii][jj] -= 1
                        if indeg[ii][jj] == 0: queue.append((ii, jj))
            ans += 1
        return ans