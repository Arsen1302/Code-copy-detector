class Solution:
	def solution_1019_5(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        edge_prob=[]
        for i in range(n):
            edge_prob.append([])
        for i in range(len(edges)):
            edge_prob[edges[i][0]].append([edges[i][1],succProb[i]])
            edge_prob[edges[i][1]].append([edges[i][0],succProb[i]])
        
        prob=[0]*n
        pq=[]
        pq.append((-1,start))
        while pq:
            current=heapq.heappop(pq)
            if prob[current[1]]==0:
                prob[current[1]]=-current[0]
                for neighbor in edge_prob[current[1]]:
                    heapq.heappush(pq,(-neighbor[1]*prob[current[1]],neighbor[0]))
                if current[1]==end:
                    break
        return prob[end]