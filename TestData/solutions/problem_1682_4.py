class Solution:
    def solution_1682_4(self, a: int, b: int) -> int:
        ans = 0 
        for x in range(1, min(a, b)+1): 
            if a % x == b % x == 0: ans += 1
        return ans