class Solution:
    def solution_929_2(self, arr: List[int]) -> int:
        ans=[]
        d={}
        for ar in arr:
            if ar in d:
                d[ar]+=1
            else:
                d[ar]=1
        for key in d:
            if key ==d[key]:
                ans.append(key)
        if len(ans)==0:
            return -1
        return max(ans)