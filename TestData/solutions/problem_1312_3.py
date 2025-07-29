class Solution:
def solution_1312_3(self, n: int) -> int:
    ans=0
    for i in range(1,n):
        for j in range(1,n):
            c= (i**2+j**2)**0.5
            if c.is_integer() and c<=n:
                ans+=1
                
    return ans