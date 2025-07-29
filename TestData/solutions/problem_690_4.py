class Solution:
    def solution_690_4(self, time: List[int]) -> int:
        ans=0
        cnt={}
        for t in time:
            if t%60 in cnt:
                cnt[t%60]+=1
            else:
                cnt[t%60]=1
        ans+=(cnt.get(0,0)*(cnt.get(0,0)-1)//2)+(cnt.get(30,0)*(cnt.get(30,0)-1)//2)
        for i in range(1,30):
            ans+=cnt.get(i,0)*cnt.get(60-i,0)
        return ans