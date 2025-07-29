class Solution:
    def solution_1267_4(self, box: List[List[str]]) -> List[List[str]]:
        R=len(box)
        C=len(box[0])
        G=box
        for i in range(R):
            j=k=C-1
            while j>=0 and k>=0:
                if G[i][j] == '#' and G[i][k] == '.':
                    G[i][j] , G[i][k] = G[i][k] , G[i][j]
                    k-=1 ; j-=1
                elif G[i][j] == '*' and G[i][k] == '.':
                    k = j-1 ; j-=1
                elif G[i][j] == '.' and G[i][k] == '.':
                    j-=1
                else:
                    k-=1 ; j-=1
        lis=[]
        for i in range(C):
            nls=[]
            for j in range(R-1,-1,-1):
                nls.append(G[j][i])
            lis.append(nls)
        return lis