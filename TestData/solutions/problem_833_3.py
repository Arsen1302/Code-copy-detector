class Solution:
    def solution_833_3(self, M: List[List[int]]) -> str:
        L, P, [x,y], N = len(M), 1 - len(M) % 2, M[-1], [M[::2], M[1::2]]
        if all(p in N[P] for p in [[x,0],[x,1],[x,2]]) or all(p in N[P] for p in [[0,y],[1,y],[2,y]]): return ['A','B'][P]
        if all(p in N[P] for p in [[0,0],[1,1],[2,2]]) or all(p in N[P] for p in [[0,2],[1,1],[2,0]]): return ['A','B'][P]
        return ["Pending","Draw"][L == 9]
		
		
- Junaid Mansuri
- Chicago, IL