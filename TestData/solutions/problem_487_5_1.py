class Solution:
    def solution_487_5_1(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        res = []
		
        def solution_487_5_2(cur, acc):
            acc.append(cur)
            
            if cur == n:
                res.append(acc)
                return
            
            for next in graph[cur]:
                solution_487_5_2(next, list(acc))
        
        solution_487_5_2(0, [])
        
        return res