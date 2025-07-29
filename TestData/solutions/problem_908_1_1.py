class Solution:
    def solution_908_1_1(self, grid: List[List[int]]) -> int:
        graph = {}
        m, n = len(grid), len(grid[0])
        
        def solution_908_1_2(i, j):
            graph[(i, j)] = {}
            neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for each in neighbors:
                x, y = each
                if x < 0 or y < 0 or x > m - 1 or y > n - 1:
                    continue
                else:
                    graph[(i, j)][(x, y)] = 1
            
            if grid[i][j] == 1:
                if j != n - 1:
                    graph[(i, j)][(i, j + 1)] = 0
            
            elif grid[i][j] == 2:
                if j != 0:
                    graph[(i, j)][(i, j - 1)] = 0
            
            elif grid[i][j] == 3:
                if i != m - 1:
                    graph[(i, j)][(i + 1, j)] = 0
            
            else:
                if i != 0:
                    graph[(i, j)][(i - 1, j)] = 0
                    
        
        for i in range(m):
            for j in range(n):
                solution_908_1_2(i, j)
        
		# solution_908_1_3 row, col to index value in distances array
        def solution_908_1_3(x, y):
            return x * n + y
        
        def solution_908_1_4(graph):
            q = deque()
            q.append([0, 0, 0])
            distances = [float(inf)] * (m * n)
            
            while q:
                cost, x, y = q.popleft()
                if (x, y) == (m - 1, n - 1):
                    return cost
                
                idx = solution_908_1_3(x, y)
                if distances[idx] < cost:
                    continue
                
                distances[idx] = cost
                for node, nxtCost in graph[(x, y)].items():
                    nxtIndex = solution_908_1_3(node[0], node[1])
                    if distances[nxtIndex] <= cost + nxtCost:
                        continue
                    
                    distances[nxtIndex] = cost + nxtCost
                    if nxtCost == 0:
                        q.appendleft([cost, node[0], node[1]])
                    else:
                        q.append([cost + 1, node[0], node[1]])
                        
        
        def solution_908_1_5(graph):
            distances = [float(inf)] * (m * n)
            myheap = [[0, 0, 0]]
            #distances[0] = 0
            
            while myheap:
                cost, x, y = heappop(myheap)
                if (x, y) == (m - 1, n - 1):
                    return cost
                
                idx = solution_908_1_3(x, y)
                if distances[idx] < cost:
                    continue
                else:
                    distances[idx] = cost
                    for node, nxtCost in graph[(x, y)].items():
                        total = cost + nxtCost
                        nxtIndex = solution_908_1_3(node[0], node[1])
                        if distances[nxtIndex] <= total:
                            continue
                        else:
                            distances[nxtIndex] = total
                            heappush(myheap, [total, node[0], node[1]])
            
            return distances[-1]
        
        #return solution_908_1_5(graph)
        return solution_908_1_4(graph)