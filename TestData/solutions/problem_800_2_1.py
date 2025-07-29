class Solution:
    def solution_800_2_1(self, G: List[List[int]]) -> int:
    	N, V, M, self.t, self.m = len(G), set(), collections.defaultdict(int), 0, math.inf
    	print(N)
    	def solution_800_2_2(a,b,o):
    		if (a,b,o) in V or M[(a,b,o)] == 2 or self.t > self.m: return
    		if (a,b,o) == (N-1,N-2,'h'):
    			self.m = min(self.m,self.t)
    			for i in V: M[i] = 1
    			return
    		self.t, _ = self.t + 1, V.add((a,b,o))
    		if o == 'h':
    			if b + 2 != N and G[a][b+2] == 0: solution_800_2_2(a, b+1, o)
    			if a + 1 != N and G[a+1][b] == 0 and G[a+1][b+1] == 0: solution_800_2_2(a+1, b, o), solution_800_2_2(a, b, 'v')
    		elif o == 'v':
    			if a + 2 != N and G[a+2][b] == 0: solution_800_2_2(a+1, b, o)
    			if b + 1 != N and G[a][b+1] == 0 and G[a+1][b+1] == 0: solution_800_2_2(a, b+1, o), solution_800_2_2(a, b, 'h')
    		if M[(a,b,o)] == 0: M[(a,b,o)] = 2
    		self.t, _ = self.t - 1, V.remove((a,b,o))
    	solution_800_2_2(0,0,'h')
    	return -1 if self.m == math.inf else self.m