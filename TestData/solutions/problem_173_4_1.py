class Solution:
    def solution_173_4_1(self, n: int) -> int:
        memo = {}
        def solution_173_4_2(n):
            if n in memo:
                return memo[n]
            if n<2:
                memo[n] = 0
                return 0
            if n==2:
                memo[2] = 2
                return 1
            maxval = 0
            for i in range(1,n//2+1):
                maxval = max(maxval,i*solution_173_4_2(n-i),i*(n-i))
            memo[n] = maxval
            return maxval
        ans = solution_173_4_2(n)
        return ans