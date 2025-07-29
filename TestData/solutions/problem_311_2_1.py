class Solution:
    def solution_311_2_1(self, n: int) -> int:
        ans=[]
        def solution_311_2_2(l,p,index):
            if l==[]:
                ans.append(p)
            for i,v in enumerate(l):
                if v%(index+1)==0 or (index+1)%v==0:
                    solution_311_2_2(l[:i]+l[i+1:],p+[v],index+1)
        
        solution_311_2_2(list(range(1,n+1)),[],0)
        return len(ans)