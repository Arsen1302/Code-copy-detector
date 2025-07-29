class Solution:
    def solution_1002_2(self, n: int, k: int) -> int:
        
        
        u=[]
        
        for i in range(1,int(n**(0.5))+1):
            
            if n%i==0:
                u.append(i)
                
                if n//i != i:
                    u.append(n//i)
        u.sort() 
        if k<=len(u):
            return u[k-1]
        return -1