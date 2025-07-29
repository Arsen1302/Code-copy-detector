class Solution:
    def solution_822_5(self, n: int, m: int, I: List[List[int]]) -> int:
        M = [[0]*m for _ in range(n)]
        for x,y in I:
            for j in range(m): M[x][j] = 1 - M[x][j]
            for i in range(n): M[i][y] = 1 - M[i][y]
        return sum(sum(M,[]))
        
		
		
- Junaid Mansuri