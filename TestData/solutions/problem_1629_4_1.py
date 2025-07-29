class Solution:
    def solution_1629_4_1(self, edges: List[int], node1: int, node2: int) -> int:
        
        def solution_1629_4_2(graph,n):
            
            dist = [-1 for i in range(len(graph))]
            
            queue = [(n,0)]
            while queue:
                x,count = queue.pop(0)
                
                dist[x] = count
                
                for i in graph[x]:
                    if dist[i]==-1:
                        queue.append((i,count+1))
                
            return dist
        
        graph = {}
        
        for i in range(len(edges)):
            graph[i] = []
        
        for i in range(len(edges)):
            if edges[i]!=-1:
                graph[i].append(edges[i])
        
        
        li1 = solution_1629_4_2(graph,node1)
        li2 = solution_1629_4_2(graph,node2)
        
        
        ans = -1
        result = 99999999
        
        for i in range(len(edges)):
            if li1[i]!=-1 and li2[i]!=-1:
                max_dist = max(li1[i],li2[i])
                if max_dist<result:
                    result = max_dist
                    ans = i
        
        return ans