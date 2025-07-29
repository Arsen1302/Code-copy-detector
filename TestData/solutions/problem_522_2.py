class Solution:
    def solution_522_2(self, n: int, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        res = [0]*n
        for i in range(n):
            q = [i]
            visit = set()
            visit.add(i)
            step, cnt = 1, 0
            while q:
                num = len(q)
                for j in range(num):
                    node = q.pop(0)
                    for nei in g[node]:
                        if nei not in visit:
                            cnt += step
                            visit.add(nei)
                            q.append(nei)
                if q:step+=1
            res[i] = cnt
        
        return res