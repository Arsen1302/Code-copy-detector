class Solution:
    def solution_835_5(self, G: List[List[int]]) -> int:
        M, N, t = len(G), len(G[0]), 0; H = [[0]*(N+1) for _ in range(M+1)]
        for i in range(M):
            c = 0
            for j in range(N):
                c += G[i][j]; H[i+1][j+1] = H[i][j+1] + c
                for k in range(1, 1 + min(i,j)):
                    if H[i+1][j+1] - H[i-k][j+1] - H[i+1][j-k] + H[i-k][j-k] == (k+1)**2: t += 1
                    else: break
        return t + sum(map(sum,G))