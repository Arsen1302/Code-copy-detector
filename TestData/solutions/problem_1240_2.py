class Solution:
    def solution_1240_2(self, n: int, k: int) -> int:
        ans = 0
        for x in range(2, n+1): ans = (ans + k) % x
        return ans + 1