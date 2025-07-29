class Solution:
    def solution_210_5_1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:           
        def solution_210_5_2(query):
            if query[0] not in graph or query[1] not in graph: return -1
            temp,visited=[(query[0],1)],set()
            while temp:
                node,current_product=temp.pop(0)
                if node==query[1]: return current_product
                visited.add(node)
                for neighbor,value in graph[node]:
                    if neighbor not in visited:
                        temp.append((neighbor,value*current_product))
            return -1
            
        graph=collections.defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1],values[i]))
            graph[equations[i][1]].append((equations[i][0],1/values[i]))
        
        return [solution_210_5_2(q) for q in queries]