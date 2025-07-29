class Solution:
    def solution_458_3(self, N: int, M: List[List[int]]) -> int:
    	DP, M, m = [[0]*N for i in range(N)], {tuple(m) for m in M}, 0
    	for i in range(N):
    		c = 0
    		for j in range(N):
    			c = 0 if (i,j) in M else c + 1
    			DP[i][j] = c
    		c = 0
    		for j in range(N-1,-1,-1):
    			c = 0 if (i,j) in M else c + 1
    			DP[i][j] = min(DP[i][j],c)  			
    	for j in range(N):
    		c = 0
    		for i in range(N):
    			c = 0 if (i,j) in M else c + 1
    			DP[i][j] = min(DP[i][j],c)
    		c = 0
    		for i in range(N-1,-1,-1):
    			c = 0 if (i,j) in M else c + 1
    			m = max(m,min(DP[i][j],c))
    	return m
		
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com