class Solution:
    def solution_1018_2(self, s: str) -> int:
        ans = n = 0
        for c in s:
            if c == "0": 
                ans = (ans + n*(n+1)//2) % 1_000_000_007
                n = 0
            else: n += 1
        return (ans + n*(n+1)//2) % 1_000_000_007