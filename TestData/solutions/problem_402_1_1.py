class Solution(object):
    def solution_402_1_1(self, edges):
        self.parent = dict()
        
        for e in edges:
            
            f0 = self.solution_402_1_2(e[0])
            f1 = self.solution_402_1_2(e[1])
            if f0 == f1:
                return e
            
            self.parent[f0] = f1
            
    def solution_402_1_2(self, x):
        if x not in self.parent:
            return x
    
        return self.solution_402_1_2(self.parent[x])