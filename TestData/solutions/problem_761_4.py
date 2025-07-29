class Solution:
    def solution_761_4(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        adj=[[] for i in range(n)]
        dist=[-1 for i in range(n)]
        dist[0]=0
        q,vis=[],set()
        for i,j in red_edges:
            adj[i].append([j,"R"])
        for i,j in blue_edges:
            adj[i].append([j,"B"])
        q.append([0,""])
        vis.add((0," "))
        lvl=0
        while q:
            lvl+=1
            size=len(q)
            for i in range(size):
                ele=q.pop(0)
                for neigh,color in adj[ele[0]]:
                    if ele[1]!=color and (neigh,color) not in vis:
                        if dist[neigh]==-1:
                            dist[neigh]=lvl
                        else:
                            dist[neigh]=min(dist[neigh],lvl)
                        q.append([neigh,color])
                        vis.add((neigh,color))
        return dist