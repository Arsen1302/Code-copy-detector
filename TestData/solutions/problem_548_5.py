class Solution:
    def solution_548_5(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = [0] * n
        for r in grid:
            if r[0]:
                for i in range(n):
                    ans[i] += r[i]
            else:
                for i in range(n):
                    ans[i] += 1-r[i]
        ret = 0
        for i in range(n):
            ret += max(ans[-1-i], m-ans[-1-i]) * (1<<i)
        return ret