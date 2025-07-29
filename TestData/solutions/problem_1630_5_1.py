class Solution:
    def solution_1630_5_1(self, edges: List[int]) -> int:
       
        n = len(edges)
        colors = [0] * n
        dis = [0] * n

        def solution_1630_5_2(u, d):
            colors[u] = 1
            dis[u] = d
            ans = -1
            if edges[u] == -1:
                colors[u] = 2
                return -1
            if colors[edges[u]] == 0:
                ans = max(ans, solution_1630_5_2(edges[u], d + 1))
            elif colors[edges[u]] == 1:
                return dis[u] - dis[edges[u]] + 1
            colors[u] = 2
            return ans

        res = -1
        for i in range(n):
            if colors[i] == 0:
                res = max(res, solution_1630_5_2(i, 0))
        return res


s = Solution()
print(s.solution_1630_5_1([-1, 4, -1, 2, 0, 4]))