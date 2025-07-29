class Solution:
def solution_1394_3(self, edges: List[List[int]], patience: List[int]) -> int:
    
    graph = defaultdict(list)
    for e1,e2 in edges:
        graph[e1].append(e2)
        graph[e2].append(e1)
    
    dist = [-1]*len(graph)
    dist[0] = 0
    queue = [0]
    d = 0
    while queue:
        d+=2
        newq = []
        for u in queue:
            for v in graph[u]:
                if dist[v]==-1:
                    dist[v]=d
                    newq.append(v)
        queue = newq

    res = 0
    for d,p in zip(dist[1:],patience[1:]):
        k = d//p
        if(d%p==0):
            k-=1
            
        res = max(res,d+k*p)
        
    return res+1