class Solution:
    def solution_986_4_1(self):
        self.res = 0 # number of changed edges
        
    def solution_986_4_2(self, g, v, visited):
        visited[v] = 1 # v is visited
        
        for neigb in g[v]:
            if visited[neigb[0]] == 0: # if  neigb[0] (v) is not visited
                if neigb[1] == 1: # if weight = 1, then wee need change edge (we moving from root (from 0))
                    self.res += 1
                
                self.solution_986_4_2(g, neigb[0], visited)
    
    def solution_986_4_3(self, n: int, connections: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        visited = [0] * n
        
        for conn in connections:
            """
            [conn[1], 1] - conn[1] - v and 1 - weight (1 means that v has output edge)
            [conn[0], -1] - conn[0] - v and -1 - weight (-1 means that v has input edge))
            """
            g[conn[0]].append([conn[1], 1]) 
            g[conn[1]].append([conn[0], -1])
        
        self.solution_986_4_2(g, 0, visited)
        
        return self.res