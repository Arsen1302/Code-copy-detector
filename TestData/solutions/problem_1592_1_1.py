class Solution:
    def solution_1592_1_1(self, cookies: List[int], k: int) -> int:
        l = [0]*k 
        self.s = float('inf')
        def solution_1592_1_2(l,i):
            if i>=len(cookies):
                self.s = min(self.s,max(l))
                return 
            if max(l)>=self.s:
                return 
            for j in range(k):
                l[j]+=cookies[i]
                solution_1592_1_2(l,i+1)
                l[j]-=cookies[i]
        
        solution_1592_1_2(l,0)
        return self.s