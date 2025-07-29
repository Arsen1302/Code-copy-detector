class Solution:
    def solution_1629_2_1(self, edges: List[int], node1: int, node2: int) -> int:
        count,ans=len(edges),float('inf')
        graph=[[] for i in range(count)]
        reach1,reach2={},{}
        vis=set()
        reach1[node1]=0
        reach2[node2]=0
        curr=float('inf')
        for u,v in enumerate(edges):
            if v!=-1:
                graph[u].append(v)
        def solution_1629_2_2(node,reach,dist):
            for it in graph[node]:
                if it not in vis:
                    vis.add(it)
                    reach[it]=dist+1
                    solution_1629_2_2(it,reach,dist+1)
                    vis.remove(it)
            return
        vis.add(node1)
        solution_1629_2_2(node1,reach1,0)
        vis.remove(node1)
        vis.clear()
        vis.add(node2)
        solution_1629_2_2(node2,reach2,0)
        vis.remove(node2)
        for node in reach2:
            if node in reach1:
                if curr>max(reach1[node],reach2[node]):
                    ans=node
                    curr=max(reach1[node],reach2[node])
                elif curr==max(reach1[node],reach2[node]) and node<ans:
                    ans=node
                    curr=max(reach1[node],reach2[node])
        if ans==float('inf'):
            return -1
        else:
            return ans