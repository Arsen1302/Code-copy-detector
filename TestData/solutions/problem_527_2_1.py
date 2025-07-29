class Solution:
    def solution_527_2_1(self, strs: List[str]) -> int:
        def solution_527_2_2(x, y):
            if x == y:
                return True
            x = [i for i in x]
            y = [i for i in y]
            # Save the index where x[i] != y[i]
            idx = []
            for i in range(len(x)):
                if x[i] != y[i]:
                    idx.append(i)
            if len(idx) == 2:
                x[idx[0]], x[idx[1]] = x[idx[1]], x[idx[0]]

                if x == y:
                    return True
                else:
                    return False
            else:
                return False
            
        def solution_527_2_3(x, y, graph):
            graph[x].append(y)
            graph[y].append(x)
            
        # Create a graph and find the number of components, that's the answer
        graph = {i: [] for i in strs}
        visited = {i: False for i in strs}
		# Construction of graph
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
			# Check if two nodes are similar
                if solution_527_2_2(strs[i], strs[j]):
                    solution_527_2_3(strs[i], strs[j], graph)  
		# Number of components to be stored in "ans" variable
        ans = 0
		# BFS over all the words in strs
        for node in graph.keys():
            if visited[node] == False:
                ans += 1
                queue = [node]
                while queue:
                    u = queue.pop(0)
                    visited[u] = True
                    for child in graph[u]:
                        if visited[child] == False:
                            visited[child] = True
                            queue.append(child)
        return ans