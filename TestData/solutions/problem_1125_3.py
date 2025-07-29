class Solution:
    def solution_1125_3(self, tasks: List[List[int]]) -> int:
        
        t=tasks
        t.sort(key=lambda x:x[1]-x[0])
        
        
        
        n=len(t)
        
        m=t[0][1]
        for i in range(n-1):
            m=max(m+t[i+1][0],t[i+1][1])
        return m