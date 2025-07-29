class Solution:
    def solution_653_1(self, S: str, T: str) -> bool:
        L, A = [len(S), len(T)], [S,T]
        for i,p in enumerate([S,T]):
            if '(' in p:
                I = p.index('(')
                A[i] = p[0:I] + 7*p[I+1:L[i]-1]
        return abs(float(A[0])-float(A[1])) < 1E-7
		
		
- Junaid Mansuri