class Solution:
    def solution_1325_5(self, segment: List[List[int]]) -> List[List[int]]:
        f=[]
        for a,b,c in segment:
            f.append([a,c])
            f.append([b,-c])
        f.sort()
        s=0
        ft=[]
        n=len(f)
        for i in range(n-1):
            s+=f[i][1]
            if(f[i][0]!=f[i+1][0] and s!=0):
                ft.append([f[i][0],f[i+1][0],s])
        
        return ft