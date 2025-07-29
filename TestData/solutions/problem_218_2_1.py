class Solution:
    def solution_218_2_1(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3: return 0
        # to simplify the code
        def solution_218_2_2(i,j):
            return [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
        
        # first we sort all heights from the matrix and store their corresponding positions
        # heights will be [(h1,[p1, p2,...]), (h2,[p1, p2, ...]), ...]
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[heightMap[i][j]].append((i,j))
        heights = sorted(d.items())
        # initialization
        volumn, area, h_lower = 0, 0, heights[0][0]
        level = [[1 for j in range(n)] for i in range(m)]
        for h, positions in heights:
            volumn += area*(h-h_lower)
            h_lower = h
            leak = []
            for i, j in positions:
                # due to height rising, now this position may hold water
                level[i][j] = 0
                area += 1
                if i == 0 or i == m-1 or j == 0 or j == n-1 or any([level[a][b] == -1 for a, b in solution_218_2_2(i,j)]):
                    # this position is reachable from outside, therefore cannot hold water
                    leak.append((i,j))
                    level[i][j] = -1
                    area -= 1
            while leak:
                i, j = leak.pop()
                for a, b in solution_218_2_2(i,j):
                    if 0 <= a < m and 0 <= b < n and not level[a][b]:
                        # new leaking position found through DFS
                        leak.append((a,b))
                        level[a][b] = -1
                        area -= 1

        return volumn