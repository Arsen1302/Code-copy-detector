class Solution:

	def solution_916_1_1(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
		if target==1:
			if t>=1 and len(edges)>=1:
				return 0
		adj = collections.defaultdict(list)
		for i in edges:
			adj[min(i[0],i[1])].append(max(i[1],i[0]))

		def solution_916_1_2(curr, target,t):
			if curr==target:
				if t==0 or len(adj[curr])==0:
					return 1
				return 0
			if t==0:
				return 0
			for child in adj[curr]:
				prob = solution_916_1_2(child, target, t-1)/len(adj[curr])
				if prob>0: 
					return prob
			return 0
		return solution_916_1_2(1,target,t)