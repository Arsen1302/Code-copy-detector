class Solution:

    def solution_475_1(self, graph: list[list[int]]) -> bool:
	
        vis = [False for n in range(0, len(graph))]
        
        while sum(vis) != len(graph): # Since graph isn't required to be connected this process needs to be repeated

            ind = vis.index(False) # Find the first entry in the visited list that is false
            vis[ind] = True
            grp = {ind:True} # initialize first node as part of group 1
            q = [ind] # Add current index to queue
            
            while q: # Go to each node in the graph
                u = q.pop(0)

                for v in graph[u]: # Go to each vertice connected to the current node

                    if vis[v] == True: #  If visited check that it is in the opposite group of the current node
                        if grp[u] == grp[v]:
                            return False # If a single edge does not lead to a group change return false

                    else: # If not visited put v in opposite group of u, set to visited, and append to q
                        vis[v] = True
                        grp[v] = not grp[u]
                        q.append(v)
        
        return True