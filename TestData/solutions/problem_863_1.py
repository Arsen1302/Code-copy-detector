class Solution:
    def solution_863_1(self, S: str) -> int:
        L = len(S)
        DP = [[0 for _ in range(L+1)] for _ in range(L+1)]
        for i,j in itertools.product(range(L),range(L)): DP[i+1][j+1] = DP[i][j] + 1 if S[i] == S[L-1-j] else max(DP[i][j+1],DP[i+1][j])
        return L - DP[-1][-1]
		
		
- Junaid Mansuri
- Chicago, IL