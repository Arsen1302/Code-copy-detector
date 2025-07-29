class Solution:
    def solution_1716_1(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        path_b = set([bob])
        lvl_b = {bob:0}
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        n = len(amount)
        node_lvl = [0] * n
        q = deque([0])
        
        lvl = 0
        seen = set([0])
        while q:
            size = len(q)
            for _ in range(size):
                u = q.popleft()
                node_lvl[u] = lvl
                for v in g[u]:
                    if v in seen:
                        continue
                    q.append(v)
                    seen.add(v)
            lvl += 1
        b = bob
        lvl = 1
        while b != 0:
            for v in g[b]:
                if node_lvl[v] > node_lvl[b]:
                    continue
                b = v
                cost = amount[b]
                path_b.add(b)
                lvl_b[b] = lvl
                break
            lvl += 1
        # print(f"lvl_b {lvl_b} path_b {path_b}  ")
        cost_a = []
        q = deque([(0, amount[0])])
        seen = set([0])
        lvl = 1
        while q:
            size = len(q)
            for _ in range(size):
                u, pre_cost = q.popleft()
                child_cnt = 0
                for v in g[u]:
                    if v in seen:
                        continue
                    seen.add(v)
                    child_cnt += 1
                    cost = pre_cost
                    inc = amount[v]
                    if v in path_b:
                        if lvl_b[v] == lvl:
                            cost += inc//2
                        elif lvl_b[v] > lvl:
                            cost += inc
                        else:
                            cost += 0
                    else:
                        cost += amount[v]
                    q.append((v, cost))
                if child_cnt == 0:
                    cost_a.append(pre_cost)
            lvl += 1
        ans = max(cost_a)
        return ans