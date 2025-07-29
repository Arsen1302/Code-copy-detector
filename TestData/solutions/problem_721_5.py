class Solution:
    def solution_721_5(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for a, b in paths:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
            
        res = [1] * n
        for i in range(n):
            color = set()
            for nei in graph[i]:
                color.add(res[nei])
            if res[i] in color:
                for typ in range(1, 5):
                    if typ not in color:
                        res[i] = typ
                        break
        return res