class Solution:
    def solution_227_4(self, B: List[List[str]]) -> int:
        if not B[0]: return 0
        M, N, t = len(B), len(B[0]), int(B[0][0] == 'X')
        for i in range(1,M): t += (B[i-1][0],B[i][0]) == ('.','X')
        for j in range(1,N): t += (B[0][j-1],B[0][j]) == ('.','X')
        for i,j in itertools.product(range(1,M),range(1,N)): t += B[i][j] == 'X' and (B[i-1][j],B[i][j-1]) == ('.','.')
        return t
		
		
- Junaid Mansuri
- Chicago, IL