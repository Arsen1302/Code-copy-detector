class Solution:
    def solution_166_5(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        for key in graph:
            graph[key].sort()
            graph[key] = deque(graph[key])
        stack = ['JFK']
        result = []
        while stack:
            if not graph[stack[-1]]:
                result.append(stack.pop())
            else:
                stack.append(graph[stack[-1]].popleft())
        result.reverse()
        return result