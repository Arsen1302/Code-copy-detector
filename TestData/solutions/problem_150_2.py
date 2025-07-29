class Solution:
    def solution_150_2(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        
        graph = defaultdict(set)
        for src, dst in edges:
            graph[src].add(dst)
            graph[dst].add(src)
        
        leaves = [node for node in graph if len(graph[node]) == 1]
        
        while n > 2:
            n -= len(leaves)
            temp = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    temp.append(neighbor)
            leaves = temp
        return leaves