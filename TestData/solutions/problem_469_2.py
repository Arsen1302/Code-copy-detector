class Solution:
    def solution_469_2(self, N, K):
        if K == 1: return 0
        if K &amp; 1: return self.solution_469_2(N - 1, K // 2 + 1)
        return self.solution_469_2(N - 1, K // 2) ^ 1