class Solution:
    def solution_1361_2_1(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        visited = {}
        rows, cols = len(land), len(land[0])
        
        def solution_1361_2_2(i, j):
            q = deque([(i, j)])
            max_i, max_j = i, j
            while q:
                i, j = q.popleft()
                max_i, max_j = max(max_i, i), max(max_j, j)
                for a, b in ((0, 1), (1, 0)):
                    u, v = i + a, j + b
                    if 0 <= u <= rows - 1 and 0 <= v <= cols - 1 and land[u][v] and (u, v) not in visited:
                        visited[(u, v)] = 1
                        q.append((u, v))
            return max_i, max_j
        
        for i in range(rows):
            for j in range(cols):
                if land[i][j] and (i, j) not in visited:
                    visited[(i, j)] = 1
                    x, y = solution_1361_2_2(i, j)
                    res.append([i, j, x, y])
        return res