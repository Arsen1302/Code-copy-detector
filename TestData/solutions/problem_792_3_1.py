class Solution:
    def solution_792_3_1(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    
        graph = defaultdict(list)
        for node1, node2 in connections:
            graph[node1].append(node2), graph[node2].append(node1)
            
        arrival_time = [None]*n
        critical_connections = []
        def solution_792_3_2(node = 0, parent = -1, time = 1):
            if arrival_time[node]: return
            arrival_time[node] = time
            for neighbour in graph[node]:
                if neighbour == parent: continue 
                solution_792_3_2(neighbour, node, time + 1)
                if arrival_time[neighbour] == time + 1: critical_connections.append((node, neighbour))
                else: arrival_time[node] = min(arrival_time[node], arrival_time[neighbour])
            return critical_connections
        
        return solution_792_3_2()