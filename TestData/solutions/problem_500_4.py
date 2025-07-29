class Solution:
    
    def solution_500_4(self, p: List[List[int]]) -> float:
        res=0
        n=len(p)
        r,l=0,0
        for i in range (1,n-1):
            for r in range(0,i):
                for l in range(i+1,n):
                    newArea=(p[i][0]*p[r][1] + p[r][0]*p[l][1] +p[l][0]*p[i][1] - p[i][0]*p[l][1] - p[r][0]*p[i][1] - p[l][0]*p[r][1] )/2
                    newArea=abs(newArea)
                    print(newArea)
                    if newArea>res:
                        res=newArea
        return res