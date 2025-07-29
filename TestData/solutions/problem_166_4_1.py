class Solution:
    def solution_166_4_1(self, tickets: list[list[str]]) -> list[str]:
        graph = {}
        for s, d in tickets:
            if d not in graph:
                graph[d] = []
            if s in graph:
                graph[s].append(d)
                graph[s].sort()
                continue
            graph[s] = [d]

        def solution_166_4_2(source, graph, visited, totalLen):
            if len(visited) == totalLen:
                return True, [source]
            choices = graph[source]
            for i in choices:
                if visited.count((source, i)) == choices.count(i):
                    continue
                visited.append((source, i))
                flag, li = solution_166_4_2(i, graph, visited, totalLen)
                if flag:
                    return True, [source] + li
                visited.pop()
            return False, []

        flag, itinerary = solution_166_4_2("JFK", graph, [], len(tickets))
        return itinerary