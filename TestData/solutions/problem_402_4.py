class Solution:
    def solution_402_4(self, edges: List[List[int]]) -> List[int]:
        # drop out indegree == 1, and check from the bottom return first indegree==2
        n = len(edges)
        indegree = collections.defaultdict(int) # SC: O(|V|)
        graph = collections.defaultdict(list) # SC: O(|V|+|E|)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        # find indegree == 1
        queue = collections.deque([i for i,v in indegree.items() if v==1])
        while queue: # TC: O(|V|+|E|), explore all vertices and edges
            node = queue.popleft()
            indegree[node] -= 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    queue.append(nei)
        # find first indegree == 2 edges from the end
        for a, b in edges[::-1]:
            if indegree[a] == 2 and indegree[b]:
                return [a,b]