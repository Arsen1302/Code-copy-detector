class Solution:
    def solution_1481_4(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]
        onecount=0
        for i in range(n):
            onecount+=(nums[i]==1)
        m=onecount
        for i in range(n):
            onecount+=(nums[i]==0)-(nums[i]==1)
            if onecount>=m:
                if onecount!=m:
                    m=onecount
                    res=[]
                res+=[i+1]
        return res