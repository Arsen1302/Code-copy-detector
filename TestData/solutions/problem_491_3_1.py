class Solution:
    def solution_491_3_1(self, graph):
        N = len(graph)
        dp = [-1] * N
        def solution_491_3_2(x):
            if dp[x] != -1: return dp[x]
            dp[x] = 0
            for i in graph[x]:
                if solution_491_3_2(i) == 0:
                    return 0
            dp[x] = 1
            return 1
        return [i for i in range(N) if solution_491_3_2(i)]