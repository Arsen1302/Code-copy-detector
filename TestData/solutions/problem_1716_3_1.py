class Solution:
    def solution_1716_3_1(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        parent = [-1 for i in range(n)]
        dist = [0 for i in range(n)]
        graph = [[] for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def solution_1716_3_2(curr,currParent):
            for it in graph[curr]:
                if it!=currParent:
                    dist[it] = dist[curr] + 1
                    solution_1716_3_2(it,curr)
                    parent[it] = curr
            return
        def solution_1716_3_3(currBob,currDist):
            while currBob!=0:
                if currDist < dist[currBob]:
                    amount[currBob] = 0
                elif currDist == dist[currBob]:
                    amount[currBob] = amount[currBob]//2
                currBob = parent[currBob]
                currDist+=1
            return
        def solution_1716_3_4(curr,currParent):
            if len(graph[curr]) == 1 and curr > 0:
                return amount[curr]
            val = -math.inf
            for it in graph[curr]:
                if it!=currParent:
                    val = max(val,solution_1716_3_4(it,curr))
            return val + amount[curr] 
                    
        solution_1716_3_2(0,-1)
        solution_1716_3_3(bob,0)
        return solution_1716_3_4(0,-1)