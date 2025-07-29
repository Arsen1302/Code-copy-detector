class Solution:
    def solution_386_3(self, I: List[List[int]]) -> List[List[int]]:
        n=len(I) ; m=len(I[0]) ; ANS=[[0]*m for i in range(n)]
        for i,j in product(range(n), range(m)):
            s=[]
            for x,y in product(range(max(0,i-1),min(i+2,n)),range(max(0,j-1),min(j+2,m))): s.append(I[x][y])
            ANS[i][j]=sum(s)//len(s)
        return ANS