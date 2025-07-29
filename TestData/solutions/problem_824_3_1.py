class Solution:
    def solution_824_3_1(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        count = 0
        def solution_824_3_2(y, x, state):
            grid[y][x] = 1
            for dy, dx in directions:
                ny, nx = y+dy, x+dx
                if ny >= h or ny < 0 or nx >= w or nx < 0:
                    state = 0
                else:
                    if grid[ny][nx] == 0 and not solution_824_3_2(ny, nx, state):
                        state = 0
            return state
        for j in range(h):
            for i in range(w):
                if grid[j][i] == 0:
                    count += solution_824_3_2(j, i, 1)
        return count