class Solution:
    def solution_151_3_1(self, nums):
        nums = [1] + nums + [1]
        @cache
        def solution_151_3_2(l,r):
            return max((solution_151_3_2(l,k-1)+nums[l-1]*nums[k]*nums[r+1]+solution_151_3_2(k+1,r) for k in range(l,r+1)),default=0)
        return solution_151_3_2(1,len(nums)-2)