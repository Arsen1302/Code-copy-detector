class Solution:
    def solution_916_5_1(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        def solution_916_5_2():
            adj = collections.defaultdict(list)
            for a, b in edges:
                adj[a].append(b)
                adj[b].append(a)
            return adj

        def solution_916_5_3(node, cumprob, time):
            canjump = sum(1 for neigh in adj[node] if neigh not in visited)
            if node==target:
                if (time <= t and not canjump) or (time==t and canjump):
                    self.ans = cumprob
                return
            visited.add(node)
            if canjump:
                prob = 1/canjump
            else:
                return
            for neigh in adj[node]:
                if neigh not in visited:
                    solution_916_5_3(neigh, cumprob * prob, time+1)

        visited = set()
        adj = solution_916_5_2()
        self.ans = 0
        solution_916_5_3(node=1, cumprob=1, time=0)
        return self.ans