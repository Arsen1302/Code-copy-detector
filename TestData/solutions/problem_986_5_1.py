class Solution:
    def solution_986_5_1(self, n: int, connections: List[List[int]]) -> int:
        in_, out = dict(), dict()
        for u, v in connections: 
            out.setdefault(u, []).append(v)
            in_.setdefault(v, []).append(u)
        
        def solution_986_5_2(n): 
            """Return required number of reverses"""
            seen[n] = True
            ans = sum(not seen[x] for x in out.get(n, []))
            for nn in in_.get(n, []) + out.get(n, []): 
                if not seen[nn]: ans += solution_986_5_2(nn)
            return ans 
        
        seen = [False]*n
        return solution_986_5_2(0)