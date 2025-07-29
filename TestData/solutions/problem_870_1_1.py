class Solution:
    def solution_870_1_1(self, n: int, connections: List[List[int]]) -> int:
        self.components = n
        # We need atleast n-1 connections to connect n networks
        if(len(connections) < n-1):
            return -1
        # If we have n-1 connections, we only need to count to number of components
        # Union-Find 
        
        parent = [i for i in range(0, n)]
        rank = [0] * n
        for x, y in connections:
            self.solution_870_1_3(x, y, parent, rank)
        # we require no. of components - 1 edge to connect n components
        return self.components - 1             
        
    def solution_870_1_2(self, x, parent):
        if(parent[x] != x):
            parent[x] = self.solution_870_1_2(parent[x], parent)
        return parent[x]
    
    def solution_870_1_3(self, x, y, parent, rank):
        parent_x = self.solution_870_1_2(x, parent)
        parent_y = self.solution_870_1_2(y, parent)
        
        if(parent_x == parent_y):
            return
        rank_x = rank[parent_x]
        rank_y = rank[parent_y]
        
        if(rank_x > rank_y):
            parent[parent_y] = parent_x
        elif(rank_x < rank_y):
            parent[parent_x] = parent_y
        else:
            parent[parent_y] = parent_x
            rank[parent_x] += 1
        self.components -= 1