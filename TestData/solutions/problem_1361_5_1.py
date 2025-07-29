class Solution:
    def solution_1361_5_1(self, land: List[List[int]]) -> List[List[int]]:

        n, m = len(land), len(land[0])
        visited = set()
        res = []

        def solution_1361_5_2(r, c , max_coords):

            if r < 0 or c < 0 or r >= n or c >= m or (r, c) in visited or land[r][c] == 0:
                return
            
            visited.add((r, c))
            max_coords[0] = max(max_coords[0], r)
            max_coords[1] = max(max_coords[1], c)

            solution_1361_5_2(r + 1, c, max_coords)
            solution_1361_5_2(r, c + 1, max_coords)
            solution_1361_5_2(r - 1, c, max_coords)
            solution_1361_5_2(r, c - 1, max_coords)
        
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1 and (i, j) not in visited:
                    start = [i, j]
                    end = [-1, -1]
                    solution_1361_5_2(i, j, end)
                    res.append(start+end)
        
        return res