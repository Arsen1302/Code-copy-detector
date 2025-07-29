class Solution:
    def solution_1508_2_1(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        
        graph = defaultdict(list)
        for f, t in edges:
            graph[t].append(f)
        
        memo = defaultdict(list)
        def solution_1508_2_2(src):
            if src in memo:
                return memo[src]
            
            for nei in graph[src]:
                memo[src] += [nei]+solution_1508_2_2(nei)
            
            memo[src] = list(set(memo[src]))
            return memo[src]
        
        for i in range(n):
            solution_1508_2_2(i)
        return [sorted(memo[i]) for i in range(n)]