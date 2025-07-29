class Solution:
    def solution_880_3_1(self, s: str) -> int:
        def solution_880_3_2():
            i,j,n=0,len(s)-1,len(s)//2
            while i<=n:
                yield (s[i], s[j])
                i+=1
                j-=1
                
        return 1 if all(x==y for x,y in solution_880_3_2()) else 2