class Solution:
    def solution_491_5(self, graph: List[List[int]]) -> List[int]:
        """
        1. find all nodes that do not have outgoing edges -> terminal node
        2. reverse all edges
        3. from each terminal node, do BFS/DFS, the node we are reaching at the end are safe nodes
        """
        q = deque()
        visited = set()
        
        # counts how many times a node is left to reach
        cnt = Counter()
        
        n_table = defaultdict(list)
        for i, neighbors in enumerate(graph):
            # count how many outgoing edges, -1 when reached
            cnt[i] = len(neighbors)
            # record reverse edge
            for n in neighbors:
                n_table[n].append(i)
            if len(neighbors) == 0:
                # no outgoing edges, set as start
                q.append(i)
                visited.add(i)

        res = []
        
        while q:
            curr = q.popleft()
            
            res.append(curr)
            
            for neighbor in n_table[curr]:
                cnt[neighbor] -= 1
                if neighbor not in visited and cnt[neighbor] == 0:
                    q.append(neighbor)
                    visited.add(neighbor)
                    
        return sorted(res)