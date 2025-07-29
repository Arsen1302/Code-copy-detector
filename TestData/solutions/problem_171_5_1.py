class Solution:
    def solution_171_5_1(self, n: int) -> List[int]:
        res = [0]*(n+1)
        
        def solution_171_5_2(n):
            if n==0: return 0
            if n==1: return 1
            
            if n%2==0: return solution_171_5_2(n//2)
            else: return 1+ solution_171_5_2(n//2)
        
        for i in range(n+1):
            res[i]=count(i)
        
        return res