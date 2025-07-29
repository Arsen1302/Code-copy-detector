class Solution:
    
    def solution_1414_5_1(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        d = defaultdict(list)
        n = len(values)
        
        for edge in edges:
            d[edge[0]].append([edge[1], edge[2]])
            d[edge[1]].append([edge[0], edge[2]])
        
        visited = [0]*n
        ans = 0
        
        def solution_1414_5_2(node, curTime, total):
            nonlocal ans
            if curTime > maxTime:
                return
            
            if visited[node] == 0:
                total+= values[node]
            
            if node == 0:
                if total > ans:
                    ans = total
            
            visited[node] += 1
            
            for vertex, time in d[node]:
                solution_1414_5_2(vertex, curTime + time, total)
            
            visited[node] -= 1
            
        solution_1414_5_2(0, 0, 0)
        return ans