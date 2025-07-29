class Solution:
    def solution_1716_5_1(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount) # number of nodes
        graph = [set() for _ in range(n)] # adjacency list presentation of the tree
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        bobpath = dict() # use hashmap to record nodes on the path from bob to root 0 
                         # as well as time: node = key, time = value
        self.stop = False # True when Bob reaches root 0, this helps stop the DFS
        visited = [False]*n # True if node is visited, initialized as False for all nodes
        def solution_1716_5_2(node,time): # the first backtracking, with time at each node
            bobpath[node] = time # add node:time to the hashmap
            visited[node] = True # mark node as visited
            if node==0: # root 0 is reached
                self.stop = True # this helps stop the DFS
                return None
            count = 0 # this helps determine if a node is leaf node
            for nei in graph[node]: 
                if not visited[nei]:
                    count += 1
                    break
            if count==0: # node is leaf node if all neighbors are already visited
                del bobpath[node] # delete leaf node from hashmap before retreating from leaf node
                return None
            for nei in graph[node]: # explore unvisited neighbors of node
                if self.stop: return None # if root 0 is already reached, stop the DFS
                if not visited[nei]:
                    solution_1716_5_2(nei,time+1)
            if not self.stop: # if root 0 is reached, keep node in the hashmap when backtracking
                del bobpath[node] # otherwise, delete node before retreating
            return None

        solution_1716_5_2(bob,0) # execute the first backtracking, time at bob is initialized = 0

        self.ans = float(-inf) # answer of the problem
        self.income = 0 # income of Alice when travelling to leaf nodes, initialized = 0
        visited = [False]*n # True if node is visited, initialized as False for all nodes
        def solution_1716_5_3(node,time): # second backtracking, with time at each node
            visited[node] = True
            if node in bobpath: # if the node Alice visits is on Bob's path, there are 3 cases
                if time == bobpath[node]: # Alice and Bob reach the node at the same time
                    reward = amount[node]//2
                elif time<bobpath[node]: # Alice reachs node before Bob
                    reward = amount[node]
                else: # Alice reachs node after Bob
                    reward = 0
            else: # if the node Alice visits is not on Bob's path
                reward = amount[node]
            self.income += reward # add the reward (price) at this node to the income
            count = 0 # this helps determine if a node is leaf node
            for nei in graph[node]:
                if not visited[nei]:
                    count += 1
                    break
            if count==0: # node is leaf node if all neighbors are already visited
                self.ans = max(self.ans,self.income) # update the answer
                self.income -= reward # remove the reward (price) at leaf node before backtracking
                return None
            for nei in graph[node]: # explore unvisited neighbors of node
                if not visited[nei]:
                    solution_1716_5_3(nei,time+1)
            self.income -= reward # remove the reward (price) at this node before retreating
            return None

        solution_1716_5_3(0,0) # execute the second backtracking, time at root 0 is initialized = 0

        return self.ans