class Solution:
    def solution_522_3_1(self, n: int, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        d = {i:[1, 0] for i in range(n)}
        
        def solution_522_3_2(root, prev):
            for nei in g[root]:
                if nei != prev:
                    solution_522_3_2(nei, root)
                    d[root][0] += d[nei][0]
                    d[root][1] += (d[nei][0] + d[nei][1])
        
        def solution_522_3_3(root, prev):
            for nei in g[root]:
                if nei != prev:
                    d[nei][1] = d[root][1] - d[nei][0] + (n-d[nei][0])
                    solution_522_3_3(nei, root)
        
        solution_522_3_2(0, -1)
        solution_522_3_3(0, -1)
        res = []
        for key in d:
            res.append(d[key][1])
        return res