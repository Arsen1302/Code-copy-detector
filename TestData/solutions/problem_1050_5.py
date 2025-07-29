class Solution:
    def solution_1050_5(self, n: int, edges: List[List[int]]) -> List[int]:
        # find all nodes with indegree of 0, these are the vertices that you must start from and cant be reached by anything else
        # so thats the smallest set of vertices that allow for you to dfs over all nodes
        indegrees = [0 for _ in range(n)]
        
        for a, b in edges:
            indegrees[b] += 1
        
        return [i for i in range(len(indegrees)) if indegrees[i] == 0]