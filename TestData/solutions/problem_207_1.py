class Solution:
    def solution_207_1(self, A: List[int]) -> int:
        s, n = sum(A), len(A)
        cur_sum = sum([i*j for i, j in enumerate(A)])
        ans = cur_sum
        for i in range(n): ans = max(ans, cur_sum := cur_sum + s-A[n-1-i]*n)
        return ans