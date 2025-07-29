class Solution:
    def solution_854_5_1(self, B: List[str]) -> List[int]:
        L, D, B[-1], m = len(B), {(0,0):(0,1)}, B[-1][:-1]+'0', 10**9 + 7
        def solution_854_5_2(i,j):
            if (i,j) in D: return D[(i,j)]
            if i < 0 or j < 0 or B[i][j] == "X": return (0,0)
            SP = [solution_854_5_2(x,y) for x,y in [(i-1,j),(i,j-1),(i-1,j-1)]]
            S = max(SP[i][0] for i in range(3))
            D[(i,j)] = (int(B[i][j]) + S, sum(y for x,y in SP if x == S))
            return D[(i,j)]
        (MS,MP) = solution_854_5_2(L-1,L-1)
        return [[MS,0][MP == 0], MP % m]
		
		
- Junaid Mansuri
- Chicago, IL