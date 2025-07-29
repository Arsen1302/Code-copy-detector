class Solution:
    def solution_1724_2_1(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for e in roads:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        visited = set()
        fuel = [0]
        def solution_1724_2_2(node):
            visited.add(node)
            people = 0
            for n in graph[node]:
                if n in visited:
                    continue
                p = solution_1724_2_2(n)
                people += p
                fuel[0] += ceil(p / seats)
            if not people:
                return 1
            return people + 1
        solution_1724_2_2(0)
        return fuel[0]