class Solution(object):
    def solution_151_1_1(self, nums):
        n=len(nums)
        nums.insert(n,1)
        nums.insert(0,1)
        self.dp={}
        return self.solution_151_1_2(1,nums,n)
    def solution_151_1_2(self,strt,nums,end):
        ans=0
        if strt>end:
            return 0
        if (strt,end) in self.dp:
            return self.dp[(strt,end)]
        for i in range(strt,end+1):
            lmax=self.solution_151_1_2(strt,nums,i-1)
            rmax=self.solution_151_1_2(i+1,nums,end)
            curr_coins=nums[strt-1]*nums[i]*nums[end+1]+lmax+rmax
            ans=max(ans,curr_coins)
        self.dp[(strt,end)]=ans
        return self.dp[(strt,end)]