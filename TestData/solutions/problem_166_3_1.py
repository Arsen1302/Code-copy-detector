class Solution:
    def solution_166_3_1(self, tickets: List[List[str]]) -> List[str]:
        adj={u: collections.deque() for u,v in tickets}
        res=["JFK"]
        tickets.sort()
        for u,v in tickets:
            adj[u].append(v)
        def solution_166_3_2(cur):
            if len(res)==len(tickets)+1:
                return True
            if cur not in adj:
                return False
            temp= list(adj[cur])
            for v in temp:
                adj[cur].popleft()
                res.append(v)
                if solution_166_3_2(v):
                    return res
                res.pop()
                adj[cur].append(v)
            return False
        solution_166_3_2("JFK")
        return res