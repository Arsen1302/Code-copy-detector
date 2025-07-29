class Solution:
    def solution_1203_5_1(self, nums: List[int], multi: List[int]) -> int:
        memo = {}
        def solution_1203_5_2(b,e,i):
            if i >= len(multi):
                return 0
            if (b,i) in memo:
                return memo[(b,i)]

            x= max(solution_1203_5_2(b+1,e,i+1)+nums[b]*multi[i],solution_1203_5_2(b,e-1,i+1)+nums[e]*multi[i])
            memo[(b,i)] = x
            return x
        return solution_1203_5_2(0,len(nums)-1,0)