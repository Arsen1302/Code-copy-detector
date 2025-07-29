class Solution:
    def solution_5_1_1(self, s: str) -> str:
        n=len(s)
        def solution_5_1_2(i,j):            
            while 0<=i<=j<n and s[i]==s[j]:
                i-=1
                j+=1                            
            return (i+1, j)
        
        res=(0,0)
        for i in range(n):
            b1 = solution_5_1_2(i,i)
            b2 = solution_5_1_2(i,i+1)            
            res=max(res, b1, b2,key=lambda x: x[1]-x[0]+1) # find max based on the length of the pallindrome strings.
                    
        return s[res[0]:res[1]]