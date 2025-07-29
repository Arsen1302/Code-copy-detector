class Solution:
    def solution_1306_3(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        t, b = 0, m - 1
        l, r = 0, n - 1

        result = [[0] * n for _ in range(m)]
        while t < b and l < r:
            index = []
            index += [[i,l] for i in range(t, b)] # left side
            index += [[b,j] for j in range(l, r)] # bottom side
            index += [[i,r] for i in range(b, t, -1)] # right side
            index += [[t,j] for j in range(r, l, -1)] # top side
            
            rotate = k % len(index)
            for i, (x, y) in enumerate(index):
                rx, ry = index[(i + rotate) % len(index)]
                result[rx][ry] = grid[x][y]

            t += 1
            b -= 1
            l += 1
            r -= 1
        
        return result