class Solution:
    def solution_402_5_1(self, edges: List[List[int]]) -> List[int]:
        # Union Find Algorithm #
        
        root = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)
        
        def solution_402_5_2(x):
            if x == root[x]:
                return x
            
            root[x] = solution_402_5_2(root[x])
            return root[x]
        
        
        def solution_402_5_3(n1, n2):
            r1 = solution_402_5_2(n1)
            r2 = solution_402_5_2(n2)
            
            if r1 == r2:
                return False
            
            if r1 != r2:
                if rank[r1] > rank[r2]:
                    root[r2] = r1
                    rank[r1] += 1
                else:
                    root[r1] = r2
                    rank[r2] += 1
            
            return True
        
        for u,v in edges:
            if not solution_402_5_3(u,v):
                return [u,v]