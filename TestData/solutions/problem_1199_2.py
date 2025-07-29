class Solution:
    def solution_1199_2(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0]) # dimensions 
        
        ans = [[-1]*n for _ in range(m)]
        queue = deque()
        for i in range(m): 
            for j in range(n):
                if isWater[i][j]:
                    queue.append((i, j))
                    ans[i][j] = 0

        while queue: 
            i, j = queue.popleft()
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and ans[ii][jj] == -1: 
                    ans[ii][jj] = 1 + ans[i][j]
                    queue.append((ii, jj))
        return ans