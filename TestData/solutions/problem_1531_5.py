class Solution:
    def solution_1531_5(self, s: str) -> int:
        ans = n0 = n1 = n01 = n10 = 0 
        for ch in s: 
            if ch == '0': 
                ans += n01
                n10 += n1
                n0 += 1
            else: 
                ans += n10
                n01 += n0 
                n1 += 1
        return ans