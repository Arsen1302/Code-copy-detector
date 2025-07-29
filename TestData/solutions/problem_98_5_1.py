class Solution:
    def solution_98_5_1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = defaultdict(list)
        for x in prerequisites:
            preq[x[0]] += [x[1]]

        order = []
        visited = {}
        def solution_98_5_2(node):
            if node in visited:
                return visited[node]
            visited[node] = True
            for n in preq[node]:
                if solution_98_5_2(n): return True
            visited[node] = False
            order.append(node)
            return False
            
        for i in range(numCourses):
            if solution_98_5_2(i): return []
            
        return order