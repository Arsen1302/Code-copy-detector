class Solution:
    def solution_1439_2_1(self, bombs: List[List[int]]) -> int:
        graph = [[] for _ in bombs]
        for i, (xi, yi, ri) in enumerate(bombs): 
            for j, (xj, yj, rj) in enumerate(bombs): 
                if i < j: 
                    dist2 = (xi-xj)**2 + (yi-yj)**2
                    if dist2 <= ri**2: graph[i].append(j)
                    if dist2 <= rj**2: graph[j].append(i)
        
        def solution_1439_2_2(x):
            """Return connected components of x."""
            ans = 1
            seen = {x}
            stack = [x]
            while stack: 
                u = stack.pop()
                for v in graph[u]: 
                    if v not in seen: 
                        ans += 1
                        seen.add(v)
                        stack.append(v)
            return ans 
        
        return max(solution_1439_2_2(x) for x in range(len(bombs)))