class Solution:
    def solution_1125_4_1(self,time,tasks):
        for f,r in tasks:
            if time<r:
                return False
            else:
                time-=f
        return time>=0
    def solution_1125_4_2(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:(x[1]-x[0]),reverse=True)
        sumTime=0
        maxReq=0
        for task in tasks:
            sumTime+=task[1]
            maxReq=max(maxReq,task[1])
        low,high=maxReq,sumTime
        ans=0
        while low<=high:
            mid=(low+high)>>1
            if self.solution_1125_4_1(mid,tasks):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans