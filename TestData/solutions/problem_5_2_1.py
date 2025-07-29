class Solution:
    def solution_5_2_1(self, s: str) -> str:
        n=len(s)
        def solution_5_2_2(i,j):            
            while 0<=i<=j<n and s[i]==s[j]:
                i-=1
                j+=1                
            
            return (i+1, j)                
        
        res=max([solution_5_2_2(i,i+offset) for i in range(n) for offset in range(2)], key=lambda x: x[1]-x[0]+1)
        
        return s[res[0]:res[1]]