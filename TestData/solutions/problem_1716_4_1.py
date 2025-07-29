class Solution:
    def solution_1716_4_1(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        path = [[bob, 0]]
        bobSteps = dict()
        aliceMaxScore = float('-inf')

        def solution_1716_4_2(parent, root, steps):
            if root == 0:
                for node, step in path:
                    bobSteps[node] = step
                return
            for child in adj[root]:
                if child == parent:
                    continue
                path.append([child, steps + 1])
                solution_1716_4_2(root, child, steps + 1)
                path.pop()
        
        def solution_1716_4_3(parent, root, steps, score):
            nonlocal aliceMaxScore
            if (root not in bobSteps) or (steps < bobSteps[root]):
                score += amount[root]
            elif steps > bobSteps[root]:
                score += 0
            elif steps == bobSteps[root]:
                score += amount[root] // 2
            
            if (len(adj[root]) == 1) and (root != 0):
                aliceMaxScore = max(aliceMaxScore, score)
                return
            
            for neighbor in adj[root]:
                if neighbor == parent:
                    continue
                solution_1716_4_3(root, neighbor, steps + 1, score)

        solution_1716_4_2(-1, bob, 0)
        solution_1716_4_3(-1, 0, 0, 0)
        return aliceMaxScore