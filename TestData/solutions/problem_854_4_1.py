class Solution:
    def solution_854_4_1(self, B: List[str]) -> List[int]:
        L, A, B[-1], m = len(B), [0,0], B[-1][:-1]+'0', 10**9 + 7
        def solution_854_4_2(i,j,s):
            if (i,j) == (0,0): [A[0],A[1]] = [s,1] if s > A[0] else [s,A[1]+1] if s == A[0] else A
            elif B[i][j] != 'X': [0<=x<L and 0<=y<L and solution_854_4_2(x,y,s+int(B[i][j])) for x,y in [(i-1,j),(i,j-1),(i-1,j-1)]]
        solution_854_4_2(L-1,L-1,0)
        return [A[0], A[1] % m]