class Solution:
    def solution_1135_5(self, n: int) -> int:
        ans = k = 0
        for x in range(1, n+1): 
            if not x &amp; x-1: k += 1
            ans = ((ans << k) + x) % 1_000_000_007
        return ans