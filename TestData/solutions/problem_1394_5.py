class Solution:      
	def solution_1394_5(self, edges: List[List[int]], patience: List[int]) -> int:
		n=len(patience)
		G=[[] for _ in range(n)]
		for x,y in edges:
			G[x].append(y)
			G[y].append(x)
		vis,q=[False]*n,[0]
		vis[0]=True
		res,d=0,1
		while q:
			new_q=[]
			for node in q:
				for child in G[node]:
					if not vis[child]:
						res=max(res,2*d+((2*d-1)//patience[child])*patience[child])
						vis[child]=True
						new_q.append(child)
			q=new_q
			d+=1
		return res+1