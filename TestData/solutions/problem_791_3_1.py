class Solution:
    def solution_791_3_1(self,ans):
        max_sum_so_far, max_ending_here = ans[0], ans[0]

        for i in ans[1:]:
            max_ending_here = max(max_ending_here+i,i)
            max_sum_so_far = max(max_sum_so_far,max_ending_here)

        return max_sum_so_far

    def solution_791_3_2(self, arr, k):
        if k == 1:
            return self.solution_791_3_1(arr)%(10**9+7)
        else:
            return ((k-2)*max(sum(arr),0) + max(self.solution_791_3_1(arr*2),0))%(10**9+7)