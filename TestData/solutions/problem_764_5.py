class Solution:
    def solution_764_5(self, n: int) -> int:
        memo = [0, 1, 1]
        if n < 2:
            return memo[n]
        for i in range(2,n):
            memo.append(memo[-1] + memo[-2] + memo[-3])
        return memo[-1]