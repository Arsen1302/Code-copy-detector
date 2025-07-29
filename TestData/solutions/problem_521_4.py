class Solution:
    def solution_521_4(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans=list(s)
            
        for i in range(len(indices)):
            
            ind=indices[i]
            flag=True
            
            for ch in sources[i]:
                if ind>=len(s) or ch!=s[ind]:
                    flag=False
                    break
                ind+=1
            
            if flag:
                ans[indices[i]]=targets[i]#Replace the start index value with the target word and keep the rest as ''
                for j in range(indices[i]+1,ind):
                    ans[j]=''
        
        return ''.join(ans)