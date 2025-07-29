class Solution:
    def solution_208_2_1(self, n: int) -> int:
        def solution_208_2_2(n, memo):
            if n in memo:
                return memo[n]
            elif n%2:
                memo[n] = 1 + min(solution_208_2_2(n-1,memo), solution_208_2_2(n+1,memo))
                return memo[n]
            else:
                memo[n] = 1 + solution_208_2_2(n//2, memo)
                return memo[n]
       
        memo = {1:0}
        return solution_208_2_2(n, memo)