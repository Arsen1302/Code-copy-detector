class Solution:
    def solution_762_5_1(self, arr):
        @lru_cache(None)
        def solution_762_5_2(i,j):
            if j<=i:
                return 0

            res = float("inf")

            for k in range(i+1,j+1):
                res = min(res,solution_762_5_2(i,k-1) + solution_762_5_2(k,j) + max(arr[i:k])*max(arr[k:j+1]))

            return res

        return solution_762_5_2(0,len(arr)-1)