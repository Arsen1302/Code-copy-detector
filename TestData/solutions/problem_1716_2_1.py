class Solution:
    def solution_1716_2_1(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = 1 + len(edges)
        tree = [[] for _ in range(n)]
        for u, v in edges: 
            tree[u].append(v)
            tree[v].append(u)
        seen = [False] * n
        
        def solution_1716_2_2(u, d): 
            """Return """
            seen[u] = True
            ans = -inf 
            dd = 0 if u == bob else n 
            for v in tree[u]: 
                if not seen[v]: 
                    x, y = solution_1716_2_2(v, d+1)
                    ans = max(ans, x)
                    dd = min(dd, y)
            if ans == -inf: ans = 0
            if d == dd: ans += amount[u]//2
            if d < dd: ans += amount[u]
            return ans, dd+1
        
        return solution_1716_2_2(0, 0)[0]