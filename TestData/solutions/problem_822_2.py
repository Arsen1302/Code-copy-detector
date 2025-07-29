class Solution:
    def solution_822_2(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        
        row=[0]*m
        col = [0]*n
        
        
        for x,y in indices:
            
            row[x]+=1
            col[y]+=1
            
        ans=0
        for i in range(m):
            for j in range(n):
                
                if (row[i]+col[j])%2:
                    ans+=1
        return ans