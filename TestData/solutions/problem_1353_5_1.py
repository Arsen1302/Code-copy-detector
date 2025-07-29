class Solution:
    def solution_1353_5_1(self, nums: List[str]) -> str:
        self.ans=[False,'']
        self.solution_1353_5_2('',nums)
        return self.ans[1]
    def solution_1353_5_2(self,substring,nums):
        if self.ans[0] or len(substring)>len(nums[0]):return
        for i in nums:
            if i.startswith(substring):break
        else:self.ans=[True,substring+'0'*(len(nums[0])-len(substring))]
        for i in '10':self.solution_1353_5_2(substring+i,nums)