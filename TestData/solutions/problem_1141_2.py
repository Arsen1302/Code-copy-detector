class Solution:
    def solution_1141_2(self, n: int) -> int:
        ans = 0
        while n > 1: 
            ans += n//2 
            n = n//2 + (n&amp;1)
        return ans