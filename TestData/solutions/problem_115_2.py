class Solution:
    def solution_115_2(self, nums: List[int]) -> List[int]:
        dc=defaultdict(lambda:0)
        n=len(nums)//3
        for a in nums:
            dc[a]+=1
        ans=[]
        for a in dc:
            if(dc[a]>n):
                ans.append(a)
        return ans