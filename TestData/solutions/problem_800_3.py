class Solution:
    def solution_800_3(self, G: List[List[int]]) -> int:
    	N, I, DP = len(G)-1, math.inf, [[math.inf]*2 for i in range(len(G)+1)]
    	DP[N-1][0] = I if 1 in [G[N][N],G[N][N-1]] else 0
    	for j in range(N-2,-1,-1): DP[j][0] = (DP[j+1][0] + 1) if G[N][j] == 0 else I
    	for i,j in itertools.product(range(N-1,-1,-1),range(N,-1,-1)):
    		n = [G[i][j],G[i][min(j+1,N)],G[min(i+1,N)][j],G[min(i+1,N)][min(j+1,N)]]
    		DP[j][0], DP[j][1] = min(1+DP[j+1][0],1+DP[j][0]), min(1+DP[j+1][1],1+DP[j][1])
    		if 1 not in n: DP[j][0], DP[j][1] = min(DP[j][0],2+DP[j+1][1],1+DP[j][1]), min(DP[j][1],2+DP[j+1][0],1+DP[j][0])
    		if 1 in [n[0],n[1]]: DP[j][0] = I
    		if 1 in [n[0],n[2]]: DP[j][1] = I
    	return -1 if DP[0][0] == I else DP[0][0]
		
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com