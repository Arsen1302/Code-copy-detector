class Solution:        
    def solution_1629_5(self, edges: List[int], node1: int, node2: int) -> int:
        s = [(node1, 0, 0), (node2, 0, 1)]
        v = defaultdict(list)
        
        ansnode = -1
        dist = float('inf')
        
        while s:
            node, distance, source = s.pop()
            
            if not v[node]:
                v[node] = [float('inf'),float('inf')]
            elif v[node][source] != float('inf'):
                continue
            
            v[node][source] = min(v[node][source], distance) 
            
            if v[node][0] != float('inf') and v[node][1] != float('inf'):
                dmax = max(v[node][0], v[node][1])
                if dmax < dist:
                    dist = dmax
                    ansnode = node
                elif dmax == dist:
                    ansnode = min(ansnode, node)
            
            if edges[node] != -1:
                next_node = edges[node]
                s.append((next_node, distance+1, source))
    
        return ansnode