class Solution:
    def solution_378_3_1(self, cur, stored, n, mem):
        
        if cur > n or stored > n:
            return sys.maxsize
        
        if cur == n:
            return 0
        
        if (cur, stored) in mem:
            return mem[(cur, stored)]
        
        if stored == 0:
            return 1 + self.solution_378_3_1(cur, 1, n, mem)
        
        if cur != stored:
            ans = 1 + min(self.solution_378_3_1(cur + stored, stored, n, mem), self.solution_378_3_1(cur, cur, n, mem))
            
        else:      
            ans = 1 + self.solution_378_3_1(cur + stored, stored, n, mem)
            
        mem[(cur, stored)] = ans
        return ans
            
    def solution_378_3_2(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        mem = dict()
        return self.solution_378_3_1(1, 0, n, mem) # initially, we have 1'A' and 0 number of 'A's copied