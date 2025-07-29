class Solution:
    def solution_826_3(self, G: List[List[int]], k: int) -> List[List[int]]:
        M, N, P = len(G), len(G[0]), len(G)*len(G[0])
        return [[G[i%P//N][i%N] for i in range(P-k+j*N,P-k+N+j*N)] for j in range(M)]



class Solution:
    def solution_826_3(self, G: List[List[int]], k: int) -> List[List[int]]:
        M, N, H, k = len(G), len(G[0]), sum(G,[]), k % (len(G)*len(G[0]))
        I = H[-k:] + H[:-k]
        return [I[i*N:(i+1)*N] for i in range(M)]



class Solution:
    def solution_826_3(self, G: List[List[int]], k: int) -> List[List[int]]:
        M, N, P = len(G), len(G[0]), len(G)*len(G[0])
        A = [[0]*N for _ in range(M)]
        for i in range(P): A[(i+k)%P//N][((i+k)%P)%N]= G[i//N][i%N]
        return A
		


- Junaid Mansuri